import random
from core.user_agents import USER_AGENTS_LIST


class RotateUserAgentMiddleware:
    def process_request(self, request, spider):
        user_agent = random.choices(USER_AGENTS_LIST)
        request.headers['User-Agent'] = user_agent
