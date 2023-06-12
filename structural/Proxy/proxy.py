from abc import ABC, abstractmethod
from typing import Dict


class BaseSite(ABC):
    """
    Abstract class for displaying the site page number
    """
    @abstractmethod
    def get_page(self, num: int) -> str:
        pass


class Site(BaseSite):
    """
    Class for displaying the site page number
    """
    def get_page(self, num: int) -> str:
        return f'Site page {num}'


class SiteProxy(BaseSite):
    """
    Proxy class for caching the site page number
    """
    def __init__(self, site: BaseSite):
        self.__site = site
        self.__site_cache: Dict[int, str] = {}

    def get_page(self, num: int) -> str:
        page: str = ''
        if self.__site_cache.get(num) is not None:
            page = self.__site_cache[num]
            page = f'{page} from cache'
        else:
            page = self.__site.get_page(num)
            self.__site_cache[num] = page
        return page


if __name__ == '__main__':
    my_site: BaseSite = SiteProxy(Site())

    print(my_site.get_page(1))
    print(my_site.get_page(2))
    print(my_site.get_page(3))

    print(my_site.get_page(2))
    print(my_site.get_page(1))