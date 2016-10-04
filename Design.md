This is the design document for puppet-complete.

# Aims

- Provide a text editor independent autocompletion backend for puppet leveraging
  information available in the MODULEPATH. Currently, no completer for vim or
  emacs provides this. Only specialized solutions for Intellij and Eclipse
  exist.
- Provide text editor front-ends. These could either be stand-alone or YCMD based.
- Provide goto documentation functionality.

# Design

- An http wrapper for puppet parser. Puppet-parser will have to parse all the
  modules in the modulepath which will be slow and will definitely have to be
  async.
  It will probably store the path in a map structure like:
  MODULEPATH->resource types->available parameters
  The interesting problem here is invalidating the map structure when the files
  in the modulepath change.
  In the initial implementation, maybe the user can do it themselves.
  
  A flask based application can serve as a very thin http wrapper for now.
  
- A YCMD backend will have to be written to make use of the http wrapper. This
  will provide two features to begin with:
  
  - Complete parameters inside a resource block
  - Display documentation of class at point
