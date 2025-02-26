# Components

## Enabling the components in this directory

Components in this directory can be enabled by deploying them as part of the [birdhouse](https://github.com/bird-house/birdhouse-deploy/) software stack. 

To enable any component in this directory, add the absolute path to the component's directory to the `BIRDHOUSE_EXTRA_CONF_DIRS` variable in birdhouse's local environment file.

For example, if the birdhouse's local environment file contains the following definition for `BIRDHOUSE_EXTRA_CONF_DIRS`:

```shell
export BIRDHOUSE_EXTRA_CONF_DIRS="
    ./components/thredds
    ./components/weaver
    ./components/jupyterhub
"
```

and you want to enable the `marble-frontend` component which, you can update the local environment file:

```shell
export BIRDHOUSE_EXTRA_CONF_DIRS="
    ./components/thredds
    ./components/weaver
    ./components/jupyterhub
    /absolute/path/to/this/repo/marble-config/components/marble-frontend
"
```

## Component descriptions

### Marble Jupyter Image

This component sets the `JUPYTERHUB_DOCKER_NOTEBOOK_IMAGES` variable to the 
[Marble jupyterlab docker image](https://hub.docker.com/repository/docker/marbleclimate/marble-jupyter-image/general).

Note that this seetting may be overwritten if you have set this variable in the birdhouse local environment file or 
you've set `JUPYTERHUB_ENABLE_MULTI_NOTEBOOKS` in that same file to allow users to select from multiple notebooks.

If that is the case, this component will check whether the Marble jupyterlab docker image is included as one of the
options offered to your users. If not, this component will log a warning.

### Marble Node Frontend 

This component deploys a website that can be used as a frontend for the birdhouse stack. It includes pages for:

- login/logout
- viewing and updating account details
- viewing services offered by the node
- etc.

This is especially useful if you'd like a user-facing account management page that is not the one offered by the 
[Magpie](https://github.com/ouranosinc/magpie) component.

To enable this component, first download the source code from github:

```shell
git clone https://github.com/DACCS-Climate/marble-node-frontend
```

and set the `MARBLE_FRONTEND_SOURCE_DIR` variable in birdhouse's local environment file to an absolute path where that
repository is created.

```shell
export MARBLE_FRONTEND_SOURCE_DIR='/path/to/marble-node-frontend'
```

To further configure this component, you can specify an absolute path to a configuration file by setting the 
`MARBLE_FRONTEND_CONFIG_FILE` variable in birdhouse's local environment file. By default, the file named `config.toml`
at the root of the checked out Marble Node Frontend repository will be

Alternatively, you can specify configuration settings as environment variables which will be used when building the 
website by setting the `MARBLE_FRONTEND_ENV_VARS` variable in birdhouse's local environment file. For example:

```shell
export MARBLE_FRONTEND_ENV_VARS="MARBLE_FRONTEND_CONFIG__NODE_ADMIN_EMAIL='email@example.com';MARBLE_FRONTEND_CONFIG__TERMS_AND_CONDITIONS__URL='http://example.com'"
```

Note that this string should not contain double quotation marks (`"`). 

For details on configuration options see the [marble node frontend documentation](https://github.com/DACCS-Climate/marble-node-frontend).

Once enabled, the webite will be available at the location specified by `BIRDHOUSE_FQDN_PUBLIC` at the `/marble/`
sub-path.

### Marble Node Settings

This component accesses the [Marble Node Registry](https://github.com/DACCS-Climate/Marble-node-registry) and sets
various environment variables based on the details about this node present in the registry.

These variables are:

- `MARBLE_NODE_SETTINGS_NODE_NAME`: the node name
- `MARBLE_NODE_SETTINGS_NODE_DESCRIPTION`: the node description
- `MARBLE_NODE_SETTINGS_NODE_CONTACT`: a contact email address for the node
- `MARBLE_NODE_SETTINGS_NODE_REGISTRATION_STATUS`: the registration status
- `MARBLE_NODE_SETTINGS_NODE_LINKS`: all additional [links](https://github.com/DACCS-Climate/Marble-node-registry/blob/main/README.md#links) associated with the node


Note that this component will automatically match the current node to one entry in the registry using the values of the
`BIRDHOUSE_PROXY_SCHEME` and `BIRDHOUSE_FQDN_PUBLIC` variables. If this component cannot find a registry entry that is 
associated with a URL that matches those variables, it will raise an error.

This component is only useful for birdhouse deployments that are registered with the [Marble Node Registry](https://github.com/DACCS-Climate/Marble-node-registry).
