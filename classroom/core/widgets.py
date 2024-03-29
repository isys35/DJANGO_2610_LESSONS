from user_role.widgets import PermissionsSelectMultiply as UserRolePermissionsSelectMultiply


class PermissionsSelectMultiply(UserRolePermissionsSelectMultiply):
    groups_permissions = {
        "Курсы": ["courses.course", "roadmaps.roadmap"],
        "Пользователи и роли": ["user_role.role", "core.user"]
    }
