# -*- coding: utf-8 -*-
from fabric.api import local


def make_virtualenv():
    ''' virtualenv-2.6 --no-site-packages -p `which python2.6`
    '''
    local("virtualenv-2.6 --no-site-packages -p `which python2.6`")


def install_requirements():
    ''' pip install -r requirements.txt
    '''
    local("./bin/pip install -r requirements.txt")


def use_profile(profile="production.cfg"):
    ''' Use a profile from the profiles folder
    '''
    local("ln -sf profiles/%s buildout.cfg" % profile)


def buildout():
    ''' Use a profile from the profiles folder
    '''
    local("./bin/buildout")


def quickstart():
    ''' Quickly start this project
    '''
    make_virtualenv()
    install_requirements()
    use_profile()
    buildout()
