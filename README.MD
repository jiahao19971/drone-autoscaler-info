# Drone CI CLI with Autoscaler
Drone cli request to obtain all autoscaler instance information

## Prerequisite 
1. Make to have python >= 3.8.5 
2. Make sure to have [drone cli](https://docs.drone.io/cli/install/) install
3. `pip install -r requirements.txt`
4. [Create a .env](#env)

### .env
```diff
+  By default, this file should be stored in ./.env

DRONE_SERVER=<URL of your drone server>
DRONE_TOKEN=<Admin access user token>
DRONE_AUTOSCALER=<URL of your drone autoscaler server>
```

## To run this script
`python drone.py`