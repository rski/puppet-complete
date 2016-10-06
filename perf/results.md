# Compiling all manifests present in $modulepath
When using `puppet parser dump`, the parsing of all manifests is really slow.

In an environment with just the puppetlabs-apache module installed:

- Roughly 130 puppet manifests present
- Time taken to dump the ASTs:

    python dump.py > /dev/null  56,30s user 3,67s system 98% cpu 1:00,67 total


On an environment containing a number of the OpenStack modules and their dependencies:

- Rougly 700 manifests present
- Time taken to dump the ASTs:

    time python dump.py > /dev/null
    real  14m6.197s
    user  13m2.212s
    sys   0m57.767s

Obviously this approach is a no-go

# Compiling only manifests used in the current file

Ok-ish, it still take 1s/file so if a manifest uses a lot of resources things will get slow.

    $ time puppet parser dump /etc/puppet/modules/concat/manifests/fragment.pp > /dev/null
    puppet parser dump /etc/puppet/modules/concat/manifests/fragment.pp >   0,58s user 0,04s system 99% cpu 0,617 total
    $ time puppet parser dump /etc/puppet/modules/apache/manifests/init.pp > /dev/null
puppet parser dump /etc/puppet/modules/apache/manifests/init.pp > /dev/null  0,59s user 0,06s system 98% cpu 0,656 total

# Using `puppet describe` for a type

Calling describe on a type, e.g. `file` takes about 3s:

    $ time ./bin/describe.py
    ['backup', 'checksum', 'checksum_value', 'content', 'ctime', 'ensure', 'force', 'group', 'ignore', 'links', 'mode', 'mtime', 'owner', 'path', 'purge', 'recurse', 'recurselimit', 'replace', 'selinux_ignore_defaults', 'selrange', 'selrole', 'seltype', 'seluser', 'show_diff', 'source', 'source_permissions', 'sourceselect', 'target', 'type', 'validate_cmd', 'validate_replacement', 'alias', 'audit', 'before', 'consume', 'export', 'loglevel', 'noop', 'notify', 'require', 'schedule', 'stage', 'subscribe', 'tag']
    ./bin/describe.py  2.84s user 0.15s system 98% cpu 3.019 total

# Puppet c++ parser

The c++ parser might provide better performance, but given that it's experimental, it might not be very usable and compiling it from source is mandatory which will be grim in the long run
