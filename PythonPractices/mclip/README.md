
# mclip NOTES and explanations


### In order to run program make your script executable
    - to the command line write +x chmod mclip.py or mclip.command
    - to run script in the command line you need to run one of the following
        1. ./mclip agree
        2. ./mclip busy
        3. ./mclip upsell

        These are dictionary keys. They have correspinding values. For example 'agree = Yes, I agree. That sounds fine to me.'. It copies to clipboard.
        keyphrase = sys.argv[1] allow us to write second argument in the command line such as agree, busy or upsell