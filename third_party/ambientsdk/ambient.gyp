# Copyright (c) 2015 Cyanogen Inc.
{
  'targets': [
     {
       # This jar contains the library I need to use.
       # This library doesn't contain the resources needed for the library to work.
       'target_name': 'ambient_sdk_javalib_no_res',
       'type' : 'none',
       'variables': {
         'jar_path': 'ambient/lib/ambientsdk-1.5.11.jar',
       },
       'includes': ['../../build/java_prebuilt.gypi'],
     },
     {
       # This target contains my library with the resources needed.
       'target_name': 'ambient_sdk_javalib',
       'type': 'none',
       'variables': {
         'java_in_dir': 'ambient/',
         'R_package': ['com.cyngn.ambientsdk'],
         'R_package_relpath': ['com/cyngn/ambientsdk'],
         'has_java_resources': 1,
         'res_v14_skip': 1,
         'run_findbugs': 0,
       },
       'dependencies': [
         'ambient_sdk_javalib_no_res',
       ],
       'includes': [ '../../build/java.gypi' ]
     },
}
