import cv2
import numpy as np

class Densepose2Texture():
  def __init__(self):
    self.Tex_Atlas = cv2.imread('./texture.png')[:,:,::-1]/255.
    self.TextureIm  = np.zeros([24,200,200,3])

    for i in range(4):
      for j in range(6):
        self.TextureIm[(6*i+j) , :,:,:] = self.Tex_Atlas[ (200*j):(200*j+200)  , (200*i):(200*i+200) ,: ]

  def TransferTexture(self, TextureIm,im,IUV):
    U = IUV[:,:,1]
    V = IUV[:,:,2]

    R_im = np.zeros(U.shape)
    G_im = np.zeros(U.shape)
    B_im = np.zeros(U.shape)

    for PartInd in range(1,23):    ## Set to xrange(1,23) to ignore the face part.
        tex = TextureIm[PartInd-1,:,:,:].squeeze() # get texture for each part.

        R = tex[:,:,0]
        G = tex[:,:,1]
        B = tex[:,:,2]

        x,y = np.where(IUV[:,:,0]==PartInd)
        u_current_points = U[x,y]   #  Pixels that belong to this specific part.
        v_current_points = V[x,y]

        r_current_points = R[((255-v_current_points)*199./255.).astype(int),(u_current_points*199./255.).astype(int)]*255
        g_current_points = G[((255-v_current_points)*199./255.).astype(int),(u_current_points*199./255.).astype(int)]*255
        b_current_points = B[((255-v_current_points)*199./255.).astype(int),(u_current_points*199./255.).astype(int)]*255
        ##  Get the RGB values from the texture images.
        R_im[IUV[:,:,0]==PartInd] = r_current_points
        G_im[IUV[:,:,0]==PartInd] = g_current_points
        B_im[IUV[:,:,0]==PartInd] = b_current_points
    generated_image = np.concatenate((B_im[:,:,np.newaxis],G_im[:,:,np.newaxis],R_im[:,:,np.newaxis]), axis =2 ).astype(np.uint8)
    BG_MASK = generated_image==0
    generated_image[BG_MASK] = im[BG_MASK]  ## Set the BG as the old image.
    return generated_image
  
  def generate(self, image):
    # Convert PIL image(<PIL.PngImagePlugin.PngImageFile image mode=RGBA>) to opencv image
    IUV = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    im = np.zeros(IUV.shape)
    image = self.TransferTexture(self.TextureIm, im, IUV)
    return image
