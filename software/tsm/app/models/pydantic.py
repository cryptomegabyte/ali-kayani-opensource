from pydantic import AnyUrl, BaseModel


class SummaryPayloadSchema(BaseModel):
    """
    Schema for the payload
    Extends BaseModel
    field:
        url: A url
    """

    url: AnyUrl
