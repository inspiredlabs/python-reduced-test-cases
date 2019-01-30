# Reduced Test Cases & Prototyping in Python

## Working fallback snippets for OpenCV development

Jan 2019, thanks to [Frederick Ngoiya](https://www.udemy.com/pythoncv/learn/v4/t/lecture/5562384?start=15), [Carlos Cordoba](https://stackoverflow.com/posts/49584017/revisions), X

### How to use this repo

Pick through feature requirements and test or append your reduced testcases. If you're introducing new requirements, then it's advisable to write snippets that match a wholly transferable implementation. 

The code here should excersize restraint. Comment only to aid comprehension rather than feature requests or conflation.


### Installation

#### Spyder, NumPy & OpenCV

- Download [Anaconda](https://www.anaconda.com/download/#download), and run the installer
- Open terminal in your PWD install OpenCV `pip install opencv-contrib-python`
- Install Conda `conda install -c https://conda.binstar.org/menpo opencv`
- For debugging, it's essential to read the relevant documentation as versions often contain breaking changes, see: Gotchas. 
- Check Python version: `python3 -V`
- Check OpenCV version `python`, 
	- &#62;&#62;&#62; `import cv2`
	- &#62;&#62;&#62; `cv2.__version__`

- Use Spyder through `Anaconda` in Spotlight (`cmd + space`), and launch it from the GUI there.

#### Pillow, Python Image Library (fork)

For fast access to data stored in pixel formats, Pillow assists in batch processing in preperation for HAAR cascades: `pip install pillow`

- from: https://pillow.readthedocs.io/en/latest/handbook/index.html

#### MatPlotLib (for Python 3.7.1)

An object-oriented API for plotting NumPy data (from detected features and UI).

- Install MatPlotLib:
	- `python -mpip install -U pip`
	- `python -mpip install -U matplotlib`
	- `pip install --upgrade setuptools`

### Shortcuts

There's no Terminal shortcuts to `*.py` files – you can however append your PWD `&&` pseudoexecutable to your macros: `# cd /Users/~/python-opencv-facial-recognition-by-frederick-ngoiya && python haar_cap.py` 

### Gotchas 

Notable, instances include: [integer division is now float division:](https://stackoverflow.com/questions/21316968/division-in-python-2-7-and-3-3) `//` not `/`, or ['module' object has no attribute:`ORB`](https://stackoverflow.com/questions/19523803/cv2-orb-and-cv2-sift-not-defined) so we have to use `ORB_create` and argument specifics such as `int(odd)` for `cv2.GaussianBlur(img, kernel, stdev)`.

The Intel licence prohibits free commercial application of evaluation files such as HAAR.xml 
