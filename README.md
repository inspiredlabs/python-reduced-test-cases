# Reduced test cases for Python prototyping

<h2 id="#top">Working fallback snippets for OpenCV development</h2>

Jan 2019, thanks to [Edwin Diaz](https://twitter.com/thisisedwindiaz) for his digestable, reproducable style, [Frederick Ngoiya](https://www.udemy.com/pythoncv/learn/v4/t/lecture/5562384?start=15), [Rayan Slim](https://www.youtube.com/watch?v=eLTLtUVuuy4), and fellow intj [Harrison Kinsley](https://twitter.com/sentdex).


<h2 id="#how">How to use this repo</h2>

Pick through feature requirements and test or append your reduced testcases. If you're introducing new requirements, then it's advisable to write snippets that match a wholly transferable implementation. 

The code here should excersize restraint. Comment only to aid comprehension rather than feature requests or conflation.


<h3 id="#installation">Installation</h3>

#### Spyder, NumPy & OpenCV

- The suite relys on the CLI and for debugging, it's essential to read the relevant documentation as versions often contain breaking changes, see: [Gotchas](#gotchas). 
- Download [Anaconda](https://www.anaconda.com/download/#download), and run the installer
- Open terminal in your PWD install OpenCV `pip install opencv-contrib-python` 
	- Although [don't expect SIFT](https://stackoverflow.com/questions/18561910/cant-use-surf-sift-in-opencv) from this method. 
- Install Conda `conda install -c https://conda.binstar.org/menpo opencv`
- Check Python version: `python3 -V`
- Check OpenCV version `python`, 
	- &#62;&#62;&#62; `import cv2`
	- &#62;&#62;&#62; `cv2.__version__`

- Use Spyder through Anaconda in Spotlight (`cmd + space`), you'll find it from the GUI.

#### Pillow, Python Image Library (fork)

For fast access to data stored in pixel formats, Pillow assists in batch processing in preperation for HAAR cascades: `pip install pillow`

- from: https://pillow.readthedocs.io/en/latest/handbook/index.html

#### MatPlotLib (for Python 3.7.1)

An object-oriented API for plotting NumPy data (from detected features and UI).

- Install MatPlotLib:
	- `python -mpip install -U pip`
	- `python -mpip install -U matplotlib`
	- `pip install --upgrade setuptools`

<h2 id="#misc">Misc</h2>

### Shortcuts

Terminal shortcuts to `*.py` files can be written with your PWD `&&` pseudoexecutable as follows: `# cd /Users/~/python-opencv-facial-recognition-by-frederick-ngoiya && python haar_cap.py && killAll python` 

<h3 id="#gotchas">Gotchas</h3>

There are a lot of things to be mindful of when starting OpenCV. Notable, instances include:

Nesting `cv2.waitKey(0)`, `cv2.destroyAllWindows()` or `cap.release()` inside a loop will not exit properly. If the CLI hangs, you'll need to `killAll python`. It's advisable to apend this to new scripts.

For modern platforms you need to do a little [more](https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1) just to return 8Bit integer. Therefor something easy like escaping a script now becomes: `cv2.waitKey(0) & 0xFF` with the corresponding byte match of  <u>`0xFF`</u>. This results in longer expressions throughout your code. 

Notable, instances include: [integer division is now float division:](https://stackoverflow.com/questions/21316968/division-in-python-2-7-and-3-3) `//` not `/`.

['module' object has no attribute:`"ORB"`](https://stackoverflow.com/questions/19523803/cv2-orb-and-cv2-sift-not-defined) so we have to use `ORB_create`, which is specific to build numbers. 

The  docs are comprehensive, but often buggy. Note the default value <u>`None`</u> in argument in `img3 = cv.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)` from the corresponding [OpenCV tutorial](https://docs.opencv.org/4.0.0/dc/dc3/tutorial_py_matcher.html). The code remains explicit, but is missing the `outImg` argument [answered on SO in May 2017](https://stackoverflow.com/questions/31631352/typeerror-required-argument-outimg-pos-6-not-found/31631995#31631995).

You will need argument specifics such as `int(odd)` for `cv2.GaussianBlur(img, kernel, stdev)`.

NumPy arrays, by default are `np.int64`. Images must be made up of the right data type, [most](https://stackoverflow.com/questions/50319617/opencv-error-cv2-cvtcolor) applications require 8bit colour depth. Specify this in `cv2.cvtColor()` with `dtype = np.uint8` –  and, for [256 times more](https://www.diyphotography.net/8-bit-vs-16-bit-color-depth-use-matters/) the pixel information, `dtype = np.uint16` although, normalising these dimensions might not be worth the overhead. 

SIFT in the [documentation](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_matcher/py_matcher.html) is referenced as `cv2.SIFT()`, but this is now: `sift = cv2.xfeatures2d.SURF_create()` works. Although you'll need to `Set OPENCV_ENABLE_NONFREE CMake option and rebuild the library in function 'create'`.

The Intel licence prohibits free commercial application of evaluation files such as HAAR.xml 

