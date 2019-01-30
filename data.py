from __future__ import print_function
from keras.preprocessing.image import ImageDataGenerator

def adjustData(img,label):
    img = img / 255
    label = label / 255
    return (img, label)

def trainGenerator(batch_size,train_path,image_folder,label_folder,aug_dict,image_color_mode = "rgb",
                    label_color_mode = "rgb",image_save_prefix  = "image",label_save_prefix  = "label",
                   save_to_dir = "",target_size = (512,512),seed = 1):
    '''
    can generate image and label at the same time
    use the same seed for image_datagen and label_datagen to ensure the transformation for image and label is the same
    if you want to visualize the results of generator, set save_to_dir = "your path"
    '''
    image_datagen = ImageDataGenerator(**aug_dict)
    label_datagen = ImageDataGenerator(**aug_dict)
    image_generator = image_datagen.flow_from_directory(
        train_path,
        classes = [image_folder],
        class_mode = None,
        color_mode = image_color_mode,
        target_size = target_size,
        batch_size = batch_size,
        save_to_dir = save_to_dir,
        save_prefix  = image_save_prefix,
        seed = seed)
    label_generator = label_datagen.flow_from_directory(
        train_path,
        classes = [label_folder],
        class_mode = None,
        color_mode = label_color_mode,
        target_size = target_size,
        batch_size = batch_size,
        save_to_dir = save_to_dir,
        save_prefix  = label_save_prefix,
        seed = seed)
    train_generator = zip(image_generator, label_generator)
    for (img, label) in train_generator:
        img, label = adjustData(img, label)
        yield (img, label)
