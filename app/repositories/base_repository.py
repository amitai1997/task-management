from app import db


class BaseRepository:
    def __init__(self, model):
        self.model = model

    def get_by_id(self, instance_id):
        instance = self.model.query.get(instance_id)
        if instance:
            return instance

    def get_basic_by_id(self, instance_id):
        instance = self.model.query.get(instance_id)
        if instance:
            return instance

    def get_all(self, filter_params=None, sort_params=None, limit=None, offset=None):
        query = self.model.query

        if filter_params:
            query = self._apply_filters(query, filter_params)

        if sort_params:
            query = self._apply_sorting(query, sort_params)

        if limit:
            query = query.limit(limit)

        if offset:
            query = query.offset(offset)

        instances = query.all()
        return instances

    def create(self, **kwargs):
        instance = self.model(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return instance

    def update(self, instance, **kwargs):
        for key, value in kwargs.items():
            setattr(instance, key, value)
        db.session.commit()
        return instance

    def delete(self, instance):
        db.session.delete(instance)
        db.session.commit()

    def _apply_filters(self, query, filter_params):
        for field, filter_data in filter_params.items():
            for operator, value in filter_data.items():
                if operator == 'eq':
                    query = query.filter(getattr(self.model, field) == value)
                elif operator == 'lt':
                    query = query.filter(getattr(self.model, field) < value)
                elif operator == 'lte':
                    query = query.filter(getattr(self.model, field) <= value)
                elif operator == 'gt':
                    query = query.filter(getattr(self.model, field) > value)
                elif operator == 'gte':
                    query = query.filter(getattr(self.model, field) >= value)
                # Add more operators as needed

        return query

    def _apply_sorting(self, query, sort_params):
        sort_fields = sort_params.strip().split(',')
        for sort_field in sort_fields:
            sort_field = sort_field.strip()
            field, order = self._parse_sort_field(sort_field)
            if field and order:
                order_by_field = getattr(self.model, field, None)
                if order_by_field is not None and self._is_orderable_field(order_by_field):
                    if order == 'asc':
                        query = query.order_by(order_by_field.asc())
                    elif order == 'desc':
                        query = query.order_by(order_by_field.desc())
                else:
                    # Handle invalid sort field or non-orderable field error
                    raise ValueError(
                        f"Invalid or non-orderable sort field: {field}")

        return query

    def _parse_sort_field(self, sort_field):
        if sort_field.startswith('-'):
            field = sort_field[1:]
            order = 'desc'
        else:
            field = sort_field
            order = 'asc'
        return field, order

    def _is_orderable_field(self, field):
        try:
            query = self.model.query.order_by(field.asc()).limit(1)
            return True
        except BaseException as e:
            return False
