#! -*- coding:utf-8 -*-

import threading

from swf.models import Domain
from swf.utils import enum


class Actor(threading.Thread):
    """SWF Actor base class

    Actor is running through a thread in order for it's polling
    operations not to be blocking. Many actors might be ran through
    the same process.

    Usage example: implementing an activity worker or a decider
    using an actor is the typical usage

    :param  domain: Domain the Actor should interact with
    :type   domain: swf.models.Domain

    :param  task_list: task list the Actor should watch for tasks on
    :type   task_list: string

    :param  last_token: last seen task token
    :type   last_token: string
    """
    STATES = enum('RUNNING', 'STOPPED')

    def __init__(self, domain, task_list, last_token=None):
        self.state = self.STATES.STOPPED

        self._set_domain(domain)
        self.task_list = task_list
        self.last_token = last_token

    def _set_domain(self, domain):
        if not isinstance(domain, Domain):
            raise TypeError("domain arg should be swf.models.Domain instance")
        self.domain = domain

    def start(self):
        """Launches the actor

        Any class overriding actor's class should set this
        method to update actor's status to Actor.STATES.RUNNING
        """
        raise NotImplementedError

    def stop(self):
        """Stops the actor

        Sets actor's status to Actor.STATES.STOPPED, and
        waits for the last polling operation to end before
        shutting down.
        """
        self.state = self.STATES.STOPPED