from .nodes import LoadImagePath, LoadAEModel, LoadDITModel, LoadQwenVLModel, Prompt, GenerateEditedImage, SaveEditedImage

NODE_CLASS_MAPPINGS = {
    "LoadImagePath": LoadImagePath,
    "LoadAEModel": LoadAEModel,
    "LoadDITModel": LoadDITModel,
    "LoadQwenVLModel": LoadQwenVLModel,
    "Prompt": Prompt,
    "GenerateEditedImage": GenerateEditedImage,
    "SaveEditedImage": SaveEditedImage,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadImagePath": "Load Image Path",
    "LoadAEModel": "Load VAE Model",
    "LoadDITModel": "Load DIT Model",
    "LoadQwenVLModel": "Load QwenVL Model",
    "Prompt": "Prompt",
    "GenerateEditedImage": "Generate Edited Image",
    "SaveEditedImage": "Save Edited Image",
} 

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
