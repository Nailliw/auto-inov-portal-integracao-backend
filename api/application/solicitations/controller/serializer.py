from api.orm.enums import SolicitationStatusEnum


def solicitation_serializer(item):
    return {
        "solicitation_id": item.id,
        "user_id": item.user_id,
        "status": SolicitationStatusEnum(item.status.value).name,
        "created_at": item.created_at.strftime('%m/%d/%Y')
    }


def get_all_solicitation(solicitations_list):
    return [solicitation_serializer(item) for item in solicitations_list]
