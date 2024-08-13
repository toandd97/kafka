{
  // Use IntelliSense to learn about possible attributes.
  // Hover to view descriptions of existing attributes.
  // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [
        {
            "name": "Run App",
            "type": "python",
            "request": "launch",
            "program": "${workspaceRoot}/app_segment_api.py",
            "envFile": "${workspaceRoot}/.env",
            "console": "internalConsole"
        },
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "envFile": "${workspaceRoot}/.env",
            "console": "internalConsole",
            "args": [
                // "create_index_v3_for_els7"
                // "alias_make"
                // msb
                // "972e6e1d-8891-4fdb-9d02-8a7855393298"
                // pingcomshop
                // "1b99bdcf-d582-4f49-9715-1b61dfff3924"
                // msbeb
                // "87d9e1f3-6da0-415f-b418-9ba9f4fe5523"
            ],
        },
        {
            "name": "Run Schedule",
            "type": "python",
            "request": "launch",
            "program": "${workspaceRoot}/start_schedule.py",
            "envFile": "${workspaceRoot}/.env",
            "console": "internalConsole",
            "args": [
                "schedule-scan-request-segment"
            ],
        },
        {
            "name": "Run Consumer",
            "type": "python",
            "request": "launch",
            "program": "${workspaceRoot}/start_consumer.py",
            "envFile": "${workspaceRoot}/.env",
            "console": "internalConsole",
            "args": [
                "s3"
            ],
        },
  ]
}