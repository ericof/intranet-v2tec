from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from v2tec.intranet import _
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class IEndereco(model.Schema):
    """Provê campos de endereço."""

    model.fieldset(
        "endereco",
        _("Endereço"),
        fields=["endereco", "complemento", "cidade", "estado", "cep"],
    )
    endereco = schema.TextLine(
        title=_("Endereço"), description=_("Informe o endereço"), required=False
    )
    complemento = schema.TextLine(
        title=_("Complemento"),
        description=_("Informe o complemento do endereço"),
        required=False,
    )
    cidade = schema.TextLine(
        title=_("Cidade"), description=_("Informe a cidade"), required=False
    )
    estado = schema.Choice(
        title=_("Estado"),
        description=_("Informe o estado"),
        required=False,
        vocabulary="v2tec.intranet.vocabulary.estados",
    )
    cep = schema.TextLine(
        title=_("CEP"), description=_("Informe o CEP"), required=False
    )
