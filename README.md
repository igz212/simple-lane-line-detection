# simple-lane-line-detection
simple lane line detection by means of Hough Line Transform which is based on transform between Polar coordinate system and cartesian coordinate system

The Hough Transform is a simple popular technique to recognized any shape,
if you can represent that shape on a mathematical form. The purpose of the technique is to find
imperfect instances of objects within a certain class of shapes by a voting procedure.
It can detect the shape even if it is broken or distorted a little bit.  

in fact Hough space is some how a Polar coordinate system which represent (r, 0) space : 
r = x.cosß + y.sinß so its legal to say  : y = - cosß/sinß.x + r/sinß   :)))))

To represent of Lines in Hough transform we use cartesian coordinate system something like xy space as mc space; 
Which represents tuples of (slope, intercept) or in another way, we could say points of (m, c).  

and of course for each point in x,y space we have a line in mc space which is c = - xm + y

so for each line in cartesian we have point in mc and for each point in mc we have line in cartesian.
Hough transform let us transform points on a specific line as lines in mc space which have intersect in a particular
point which is (m, c), the exact transform for line which they are on. Now you see, this is awesome. :)


we have two kind of Hough Line Transform in OpenCV : 
    1. The Standard Hough Line which implemented as Hough Line
    2. The ProbabilisticHough Line Transform as HoughLinesP
    
As a matter of fact, when we use this method to find edges by canny algorithm
 and try later to use Polar coordinate system to find lines which belong to the road; we should remember,
 that in our frame would may be more line shape detected. So to avoid detect other lines in frame we could 
 use region of interest. That means we mask our image to make a region which we interested to find lines in it.
 And exactly that would be road and som area around of it. 
 to make a mask we could use an array of vertices which could make our region of interest as polygonal shape.
 If we adjust canny after making mask to our original image, we may have more unsought lines, which are error
 for lane line detection. so make canny threshold before applying mask to image.  
 
 
*** And of course, we assume that our camera would be at the same position, whole time we try to detect lane lines.
        So the region of interest may be differ case by case.  ;)
    Using HoughLine Transform is one the simple ways to detect lines. to improve accuracy we need mor complex plan
    which include detect another object to avoid highlight them as lane lines. 
    
now let's try Hough Transform step by step : 
    1. edge detection. Use canny as detector or some kind of gradient like combined Sobel
    2. Mapping of edge points to the Hough Space
    3. find lines with infinite length by means of interpretation of those points with Thresholding 
    or any possible method which you know.
    4. Conversion of infinite lines to finite lines.
    
