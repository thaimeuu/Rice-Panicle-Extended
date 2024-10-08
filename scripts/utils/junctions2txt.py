import os
from ..generate_annotations.AnnotationsGenerator import AnnotationsGenerator


def junctions2txt(img_path: str, ricepr_path: str, save_path: str, remove_end_generating: bool = False):
    """
    A utils function to interact with *generate_annotations* module
    
    This function save a text file with the encoded bounding boxes that capture junctions of a rice panicle

    Args:
        img_path (str): original image path
        ricepr_path (str): .ricepr path
        save_path (str): the parent dir. (file name will be img_name_junctions.txt)
        remove_end_generating (bool, optional): Defaults to False.
    """
    generator = AnnotationsGenerator(img_path=img_path, ricepr_path=ricepr_path)
    generator.encode_junctions(save_path=save_path, remove_end_generating=remove_end_generating)
    
    
if __name__ == "__main__":
    original_img_path = "data/raw"
    african_path = original_img_path + "/African"
    asian_path = original_img_path + "/Asian"
    
    processed_path = "data/processed"
    processed_african_path = processed_path + "/African"
    processed_asian_path = processed_path + "/Asian"
    
    remove_end_generating = False  # Change this if needed
    save_path = "test"  # Change this if needed
    
    # =============================== #
    #      Comment out if needed      #
    # =============================== #
    
    for original_img in os.listdir(african_path):
        if original_img.endswith(".jpg"):
            name = original_img.split(".")[0]
            img_path = african_path + "/" + original_img
            ricepr_path = processed_african_path + f"/{name}.ricepr"
            junctions2txt(
                img_path=img_path,
                ricepr_path=ricepr_path,
                save_path=f"{save_path}",
                remove_end_generating=remove_end_generating
            )
            break  # Change this if needed
    
    for original_img in os.listdir(asian_path):
        if original_img.endswith(".jpg"):
            name = original_img.split(".")[0]
            img_path = asian_path + "/" + original_img
            ricepr_path = processed_asian_path + f"/{name}.ricepr"
            junctions2txt(
                img_path=img_path,
                ricepr_path=ricepr_path,
                save_path=f"{save_path}",
                remove_end_generating=remove_end_generating
            )
            break  # Change this if needed
            