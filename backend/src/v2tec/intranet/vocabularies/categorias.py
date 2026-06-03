from v2tec.intranet import _
from zope.i18nmessageid import Message
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


OPCOES: list[tuple[str, Message]] = [
    ("clt", _("CLT")),
    ("pj", _("Pessoa Jurídica")),
]


@provider(IVocabularyFactory)
def vocab_categorias(context) -> SimpleVocabulary:
    """Categorias de contratação na V2Tec."""
    terms = []
    for token, title in OPCOES:
        terms.append(SimpleTerm(token, token, title))
    return SimpleVocabulary(terms)
