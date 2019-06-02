# Description

This project implements a telegram bot with built-in **[DNN classifier](https://github.com/okeer/dnn-classifier)** library and model trained on cats dataset. So, when a user sends some image to telegram bot, the bot replies with estimated probability which calculates DNN algorythm.

# Usage
[@ItIsACat](https://t.me/IsItACatBot) - already deployed telegram bot which has this code deployed. Just send some pic to it to get started.

# Deployment

This project implies integration with AWS services, more particularly - **AWS Lambda**. To deploy the set of resources, **CloudFormation** is used.

So if you want to create a bot for yourself, then use Telegram documatation and @BotFather to create one, then provision a **AWS Lambda** stack:

```
# sam build --use-container
```

```
# sam package --s3-bucket <YOUR_STACK_NAME> --output-template-file package.yaml
```

Make sure to add **API_KEY** to `package.yaml` before the last stage:

```
# aws cloudformation deploy --template-file package.yaml --stack-name <YOUR_STACK_NAME> --capabilities CAPABILITY_IAM --force-upload
```
