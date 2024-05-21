from setuptools import find_packages, setup

# minimal setup for brainscore
setup(
    name='ask-anything',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '':[
            'video_chat/*',
            'video_chat2/*',
        ]
    },
)