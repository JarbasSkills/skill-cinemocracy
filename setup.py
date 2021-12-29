#!/usr/bin/env python3
from setuptools import setup

# skill_id=package_name:SkillClass
PLUGIN_ENTRY_POINT = 'skill-cinemocracy.jarbasai=skill_cinemocracy:CinemocracySkill'

setup(
    # this is the package name that goes on pip
    name='ovos-skill-cinemocracy',
    version='0.0.1',
    description='ovos cinemocracy skill plugin',
    url='https://github.com/JarbasSkills/skill-cinemocracy',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    package_dir={"skill_cinemocracy": ""},
    package_data={'skill_cinemocracy': ['locale/*', 'ui/*']},
    packages=['skill_cinemocracy'],
    include_package_data=True,
    install_requires=["ovos_workshop~=0.0.5a1"],
    keywords='ovos skill plugin',
    entry_points={'ovos.plugin.skill': PLUGIN_ENTRY_POINT}
)
