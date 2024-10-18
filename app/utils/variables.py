from pathlib import Path


ROOT_DIR = Path(__file__).parent.parent
IMAGES_DIR = ROOT_DIR / 'resources/img'

# Images
ICON_HOME = IMAGES_DIR / "house.png"
ICON_REGISTRATION = IMAGES_DIR / "folder-1.png"
ICON_SAVE = IMAGES_DIR / "save.png"
ICON_CLEAN_FIELDS = IMAGES_DIR / "garbage.png"
ICON_UPDATE_TABLE = IMAGES_DIR / "repeat.png"

ICON_LOGO = IMAGES_DIR / "logo_opac.png"
ICON_PERSON_TYPE = IMAGES_DIR / "user.png"
ICON_NAME = IMAGES_DIR / "briefcase.png"
ICON_JOB = IMAGES_DIR / "id-card.png"
ICON_CPF = IMAGES_DIR / "file.png"
ICON_RG = IMAGES_DIR / "id-card-2.png"
ICON_EMAIL = IMAGES_DIR / "paper-plane.png"
ICON_DATE = IMAGES_DIR / "calendar.png"
ICON_PHONE = IMAGES_DIR / "smartphone.png"
ICON_CEP = IMAGES_DIR / "worldwide.png"
ICON_ADDRESS = IMAGES_DIR / "sign.png"
ICON_NUMBER = IMAGES_DIR / "sign-1.png"
ICON_UF = IMAGES_DIR / "map.png"
ICON_CITY = IMAGES_DIR / "map-location.png"




if __name__ == "__main__":
    print("root dir: --> ", ROOT_DIR)
    print("files dir: --> ", IMAGES_DIR)
    print("icon dir: --> ", ICON_NAME)
    
    
