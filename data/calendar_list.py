from data.mod1 import fe1, be1
from data.mod2 import fe2, be2
from data.mod3 import fe3, be3
from data.combined import combined
from data.community import community

calendar_list = {
    "mod1": {
        "FE": fe1,
        "BE": be1
    },
    "mod2": {
        "FE": fe2,
        "BE": be2
    },
    "mod3": {
        "FE": fe3,
        "BE": be3
    },
    "mod4": combined,
    "community": community
}
