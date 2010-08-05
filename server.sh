#!/bin/bash

case $1 in
    run)
        echo "Starting django development server..."
        python manage.py runserver
    ;;
    netrun)
        echo "Starting django development server with local network visibility..."
        python manage.py runserver 0.0.0.0:8000
    ;;
    validate)
        python manage.py validate
    ;;
    syncdb)
        python manage.py syncdb
    ;;
    test)
        ./run_tests.sh
    ;;
    newapp)
        python manage.py startapp $2
    ;;
    shell)
        python manage.py shell
    ;;
    *)
        echo "Parameter error!"
        exit 1
    ;;
esac
