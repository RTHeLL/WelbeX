from repository import Repository

repository = Repository()


class Controller:
    def get_data(self, payload):
        if payload is None:
            payload = self.__prepare_filter(payload)
        return repository.get_all_rows(payload=payload)

    @staticmethod
    def __prepare_filter(payload):
        if payload is None:
            payload = dict()
            payload['pageNo'] = 1
            payload['pageRowCount'] = 10
            payload['sortField'] = None
            payload['isDescOrder'] = True
            payload['filterField'] = None
            payload['filterValue'] = None
            payload['filterType'] = None
        return payload
