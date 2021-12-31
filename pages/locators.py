from selenium.webdriver.common.by import By

class BasePageLocators():
    TY_EXCEPTION = (By.CSS_SELECTOR, ".ty-exception")
    #################################################
    BUTTON_PRISE_LIST = (By.CSS_SELECTOR, "#toppri")
    FORM_PRISE_LIST = (By.CSS_SELECTOR, ".ui-dialog")
    GEOLOCATION_MAP = (By.CSS_SELECTOR, "#opener_geo_maps_location_dialog_3909")
    NOVINKI_LINK = (By.CSS_SELECTOR, 'a[href="https://besttea.ru/noviepostupleniya/"]')
    SALE_LINK = (By.CSS_SELECTOR, 'a[href="https://besttea.ru/sale/"]')
    KONTAKTY_LINK = (By.CSS_SELECTOR, 'a[href="/contact"]')
    class InformationListLocators():
        INFORMATION_LIST = (By.CSS_SELECTOR, "#text_links_3912 a")
        DOSTAVKA_LINK = (By.CSS_SELECTOR, "a[href='https://besttea.ru/info/dostavka/']")
        OPLATA_LINK = (By.CSS_SELECTOR, "a[href='https://besttea.ru/info/oplata/']")
        OBMEN_VOZVRAT_LINK = (By.CSS_SELECTOR, "a[href='https://besttea.ru/info/usloviya-vozvrata/']")
    class OptovikamListLocators():
        OPTOVIKAM_LIST = (By.CSS_SELECTOR, ".optovikampnkt bdi")
        CHAI_OPTOM_LINK = (By.CSS_SELECTOR, "a[href='/info/opt']")
        KOFE_OPTOM_LONK = (By.CSS_SELECTOR, 'a[href="/info/opt/kupit-kofe-optom/"]')
        POSUDA_OPTOM_LINK = (By.CSS_SELECTOR, 'a[href="/info/opt/posuda-is-stekla-optom/"]')
        PROIZVODSTVO_LINK = (By.CSS_SELECTOR, 'a[href="/proizvodstvo"]')
        CHAI_I_KOFE_POD_STM_LINK = (By.CSS_SELECTOR, 'a[href="/info/opt/stm-chay"]')
        FASOVKA_PRODUKTOV = (By.CSS_SELECTOR, 'a[href="https://besttea.ru/info/opt/uslugi-fasovki-i-upakovki-sypuchih-produktov"]')
        SERTIFIKATY_LINK = (By.CSS_SELECTOR, 'a[href="/info/sertifikatyi"]')
    class WishList():
        WISH_LIST_LINK = (By.CSS_SELECTOR, "#abt__ut2_wishlist_count")
        WISH_LIST_LINK_COUNT = (By.CSS_SELECTOR, "#abt__ut2_wishlist_count span")
    class KatalogTovarovListLocators():
        KATALOG_TOVAROV_LIST_BUTTON = (By.CSS_SELECTOR, "#sw_dropdown_3918")
        KATALOG_TOVAROV_LIST = (By.CSS_SELECTOR, ".ty-menu__item.cm-menu-item-responsive.first-lvl")
        CHAI_LINK = (By.CSS_SELECTOR, 'a[href="/elitniy-chay"]')
        KOFE_LINK = (By.CSS_SELECTOR, 'a[href="/zernovoi-kofe"]')
        MATE_LINK = (By.CSS_SELECTOR, 'a[href="/mate-i-prinadlejnosti"]')
        SLADOSTI_LINK = (By.CSS_SELECTOR, 'a[href="/sladosti"]')
        POSUDA_LINK = (By.CSS_SELECTOR, 'a[href="/posuda-i-prinadlezhnosti/"]')
        UPAKOVKA_LINK = (By.CSS_SELECTOR, 'a[href="https://besttea.ru/torgovoe-oborudovanie/"]')
    class SearchLokators():
        SERCH_INPUT = (By.CSS_SELECTOR, '#search_input')
        BUTTON_SERCH = (By.CSS_SELECTOR, '.ty-icon-search')


class MainPageLocators():
    class Bestsellers():
        PRODUCT_5 = (By.NAME, "product_form_5240003024")
        ADD_WISH_LIST_PRODUCT_5 = (By.CSS_SELECTOR, "#button_wishlist_5240003024")

class SearchPageLocators():
    SEARCH_PAGE_TEXT = (By.CSS_SELECTOR, '.span12.main-content-grid span')