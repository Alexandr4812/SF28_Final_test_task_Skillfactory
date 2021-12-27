from selenium.webdriver.common.by import By

class BasePageLocators():
    TEA_SHOP_PHONE = (By.CSS_SELECTOR, "#topteln")
    WHOLESALES_DEPERTAMENT_PHONE = (By.CSS_SELECTOR, ".opttopteln")
    BUTTON_PRISE_LIST = (By.CSS_SELECTOR, "#toppri")
    FORM_PRISE_LIST = (By.CSS_SELECTOR, ".ui-dialog")
    GEOLOCATION_MAP = (By.CSS_SELECTOR, "#opener_geo_maps_location_dialog_3909")
    NOVINKI_LINK = (By.CSS_SELECTOR, 'a[href="https://besttea.ru/noviepostupleniya/"]')
    SALE_LINK = (By.CSS_SELECTOR, 'a[href="https://besttea.ru/sale/"]')
    class InformationListLocators():
        INFORMATION_LIST = (By.CSS_SELECTOR, "#text_links_3912 a")
        DOSTAVKA_LINK = (By.CSS_SELECTOR, "a[href='https://besttea.ru/info/dostavka/']")
        OPLATA_LINK = (By.CSS_SELECTOR, "a[href='https://besttea.ru/info/oplata/']")
        OBMEN_VOZVRAT_LINK = (By.CSS_SELECTOR, "a[href='https://besttea.ru/info/usloviya-vozvrata/']")
    class OptovikamListLocators():
        OPTOVIKAM_LIST = (By.CSS_SELECTOR, ".optovikampnkt bdi")
