from pydantic import AnyHttpUrl, AnyUrl, BaseModel


class SummaryPayloadSchema(BaseModel):
    """
    Schema for the payload
    Extends BaseModel
    field:
        url: A url
    """

    url: AnyUrl


class SummaryResponseSchema(SummaryPayloadSchema):
    """
    Schema for summaries response
    Extends SummaryPayloadSchema
    """

    id: int


class SummaryUpdatePayloadSchema(SummaryPayloadSchema):
    """
    Schema for summaries update payload
    Extends SummaryPayloadSchema
    """

    summary: str


class SummaryPayloadSchema(BaseModel):
    """
    Schema for summaries payload
    Extends BaseModel
    """

    url: AnyHttpUrl
