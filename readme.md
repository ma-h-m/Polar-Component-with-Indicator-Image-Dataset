# Polar Component with Indicator Image Dataset

This is a dataset for polar component rotation detection. This dataset is based on [PCB DSLR DATASET](https://zenodo.org/record/3886553\#.ZDu-fj1By0q).

Under directory `data_set_with_indicator`, in each subdirectory, there are a few images of PCB components with a certain kind of polar indicator, and an image of that kind indicator, named `indicator.jpg`.

In `data_set_with_indicator/annotion.txt`, each line comprises component class, file path of the component image and file path of the indicator image. The prefix of the file path can be changed according to your environment.

You can also use `dataset_maker.py` to make your dataset.
