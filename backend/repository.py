from app import db
from models import Rows

from sqlalchemy import asc, desc


class Repository:
    def get_all_rows(self, payload):
        __rows = db.session.query(Rows)\
            .filter(self.__get_filter_definition(payload))\
            .order_by(self.__get_sort_definition(payload))\
            .paginate(payload['pageNo'],
                      payload['pageRowCount'],
                      False)

        __total_rows = __rows.total
        __items_rows = [i.serialize for i in __rows.items]

        return {'rows': __items_rows, 'total': __total_rows}

    def __get_filter_definition(self, payload):
        if payload['filterField'] is None:
            return Rows.id is not None

        if payload['filterType'] == 'equally':
            return self.__get_filter_definition_eq(payload)
        elif payload['filterType'] == 'contains':
            return self.__get_filter_definition_co(payload)
        elif payload['filterType'] == 'over':
            return self.__get_filter_definition_ov(payload)
        elif payload['filterType'] == 'less':
            return self.get_filter_definition_le(payload)

    @staticmethod
    def __get_filter_definition_eq(payload):
        if payload['filterField'] == 'title':
            return Rows.title == payload['filterValue']
        elif payload['filterField'] == 'count':
            return Rows.count == payload['filterValue']
        elif payload['filterField'] == 'distance':
            return Rows.distance == payload['filterValue']

    @staticmethod
    def __get_filter_definition_co(payload):
        if payload['filterField'] == 'title':
            return Rows.title.contains(payload['filterValue'])
        else:
            return Rows.id is not None

    @staticmethod
    def __get_filter_definition_ov(payload):
        if payload['filterField'] == 'title':
            return Rows.title > payload['filterValue']
        elif payload['filterField'] == 'count':
            return Rows.count > payload['filterValue']
        elif payload['filterField'] == 'distance':
            return Rows.distance > payload['filterValue']

    @staticmethod
    def get_filter_definition_le(payload):
        if payload['filterField'] == 'title':
            return Rows.title < payload['filterValue']
        elif payload['filterField'] == 'count':
            return Rows.count < payload['filterValue']
        elif payload['filterField'] == 'distance':
            return Rows.distance < payload['filterValue']

    @staticmethod
    def __get_sort_definition(payload):
        if payload['sortField'] is None:
            return Rows.id is not None

        if payload['isDescOrder']:
            return desc(payload['sortField'])
        else:
            return asc(payload['sortField'])
