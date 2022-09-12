import mock
deletePage = mock.Mock()
page = mock.Mock()
registry = mock.Mock()
logger = mock.Mock()
configKeys = mock.Mock()
E_OK = 200
E_ERROR = 500


def delete_page():
    if deletePage(page) == E_OK:
        if registry.deleteReference(page.name) == E_OK:
            if configKeys.deleteKey(page.name.makeKey()) == E_OK:
                logger.log("page deleted")
            else:
                logger.log("configKey not deleted")
        else:
            logger.log("deleteReference from registry failed")
    else:
        logger.log("delete failed")
        return E_ERROR


def _delete_page():
    try:
        deletePage(page)
        registry.deleteReference(page.name)
        configKeys.deleteKey(page.name.makeKey())
    except Exception as e:
        logger.log(e.getMessage())
