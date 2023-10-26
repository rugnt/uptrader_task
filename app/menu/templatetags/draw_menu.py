from django import template
from django.utils.html import format_html

from menu.models import TreeMenu


register = template.Library()


def generate_ul_tag_in_html(tree_menu, child_html=None, parent_name_child_html=None):
    """Генерирует ul тег по объектам модели TreeMenu, создавая из этих объектов
    li теги, и если имя тега li совпадает с parent_name_child_html, то мы вставляем
    child_html
    """
    html = '<ul>'
    for relevant_obj in tree_menu:
        if child_html is not None and relevant_obj.name == parent_name_child_html:
            html += f'<li><a href="/menu/{relevant_obj.path}">{relevant_obj.name}</a>' \
                    f'{child_html}</li>'
        else:
            html += f'<li><a href="/menu/{relevant_obj.path}">{relevant_obj.name}</a></li>'
    html += '</ul>'
    return html


@register.simple_tag
def draw_menu(path):
    if path == '':
        html = generate_ul_tag_in_html(
            TreeMenu.objects.filter(parent=None)
        )
    else:
        all_menu = list(TreeMenu.objects.select_related('parent').all())
        # Словарь, ключи которого являются id объектами модели "TreeMenu". Необходим
        # для быстрого поиска родителя
        relationships_dict = {None: None}
        cur = None

        for menu in all_menu:
            if path == menu.path:
                cur = menu
            relationships_dict[menu.id] = menu

        if cur is None:
            raise TreeMenu.DoesNotExist

        html = ""
        child_html = None
        parent_name_child_html = None

        while True:
            child_html = html

            def parent_filter(menu):
                """Фильтр объектов по родителю"""
                return menu.parent == cur

            html = generate_ul_tag_in_html(
                filter(parent_filter, all_menu),
                child_html,
                parent_name_child_html
            )

            if cur is None:
                break
            else:
                parent_name_child_html = cur.name
                cur = relationships_dict[cur.parent_id]

    return format_html(html)

