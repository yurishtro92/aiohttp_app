from aiohttp import web
from gino import Gino
import config

app = web.Application()
db = Gino()
PG_DSN = config.POSTGRE_DSN


class AdvModel(db.Model):
    __tablename__ = 'advs'
    id = db.Column(db.Integer(), primary_key=True)
    head = db.Column(db.String(), nullable=False)
    text = db.Column(db.String(), nullable=False)
    date = db.Column(db.String(), nullable=False)
    owner = db.Column(db.String(), nullable=False)


class AdvPostView(web.View):
    async def post(self):
        user_data = await self.request.json()
        new_adv = await AdvModel.create(**user_data)
        return web.json_response(
            new_adv.to_dict()
        )


class AdvGetView(web.View):
    async def get(self):
        user_data = await self.request.json()
        adv_id = user_data['id']
        adv = await AdvModel.get(adv_id)
        return web.json_response(adv.to_dict())


class AdvDeleteView(web.View):
    async def delete(self):
        user_data = await self.request.json()
        adv_id = user_data['id']
        await AdvModel(id=adv_id).delete()
        return web.json_response({'status': f'advertisement with id {adv_id} deleted'})


class AdvPatchView(web.View):
    async def patch(self):
        user_data = await self.request.json()
        adv_id = user_data['id']
        AdvModel(id=adv_id).update(**user_data)
        return web.json_response({'status': f'advertisement with id {adv_id} updated'})


async def init_orm(app):
    await db.set_bind(PG_DSN)
    await db.gino.create_all()
    yield
    await db.pop_bind().close()


app.cleanup_ctx.append(init_orm)
app.add_routes([web.post('/advertisement/post', AdvPostView),
                web.patch('/advertisement/patch', AdvPatchView),
                web.delete('/advertisement/delete', AdvDeleteView),
                web.get('/advertisement/get', AdvGetView)])
web.run_app(app, host='127.0.0.1', port=8080)
