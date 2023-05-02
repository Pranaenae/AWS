# Creating a Lex Chatbot

Give the name PersonalBanker.

![image](https://user-images.githubusercontent.com/80820244/235688849-918b9fb4-f86d-4e03-8df1-4b594d4240b6.png)

Create a new IAM role for the bot.

Choose the language and the voice.

![image](https://user-images.githubusercontent.com/80820244/235689653-f4183021-9f5c-4be7-90a1-7a8c05046649.png)

Create the chatbot.

## Create an intent.

Create the intent GetBalanceCheck.

![image](https://user-images.githubusercontent.com/80820244/235691463-2e6d1920-cb5c-4e3d-821a-734aaada2745.png)

Provide the following sample utterances.

![image](https://user-images.githubusercontent.com/80820244/235691387-f5ecc4b8-0eb5-4bd2-a04e-6c992752ba7d.png)

Add two slots to request user's account type and pin no.

![image](https://user-images.githubusercontent.com/80820244/235693285-950c933a-b657-431a-ad0b-a9a344e02721.png)

## Testing the bot

![image](https://user-images.githubusercontent.com/80820244/235694041-a14290a8-7694-498a-bb23-5d9885438d62.png)

## Create a new Lambda function.

![image](https://user-images.githubusercontent.com/80820244/235710020-41cdae8d-8842-4dce-8330-fca5f46d9108.png)

Change the role and add Harness
![image](https://user-images.githubusercontent.com/80820244/235709860-19dfab6b-5f21-4f78-9ec4-212301059bfd.png)

```
const AWS = require('aws-sdk');

// Route the incoming request based on intent.
const accounts = [
  {
    type: 'current',
    pinNumber: '1234',
    balance: '134.12',
  },
  {
    type: 'saving',
    pinNumber: '1234',
    balance: '154.12',
  },
];

// Check to see if an account matches for the account type and also that the pin number for that 
// account matches the array
const getAccount = (type, pinNumber) => {
  const result = accounts.find(account => account.type.toLowerCase() === type.toLowerCase()
  && account.pinNumber === pinNumber);
  return result;
};

const balanceIntent = (intentRequest, callback) => {
  const { slots } = intentRequest.currentIntent;
  const sessionAttributes = { ...intentRequest.sessionAttributes, ...slots };
  const account = getAccount(slots.AccountType, slots.PinNumber);

  if (!account) {
    callback(elicitSlot(sessionAttributes, 'GetBalanceCheck', slots, 'PinNumber', {
      contentType: 'PlainText',
      content: 'No accounts have been found with this pin number please re-enter your pin number',
    }));
  } else {
    callback(close(sessionAttributes, 'Fulfilled', {
      contentType: 'PlainText',
      content: `You have £${account.balance} in your account`,
    }));
  }
};

const balanceIntentError = (intentRequest, callback) => {
  const { slots } = intentRequest.currentIntent;
  const sessionAttributes = { ...intentRequest.sessionAttributes, ...slots };
  const account = getAccount(slots.AccountType, slots.PinNumber);
  callback(close(sessionAttributes, 'Fulfilled', {
    contentType: 'PlainText',
    content: `You have £${account.balance} in your account, is there anything can help you with?`,
  }));
};

// This a simple example to demonstrate how lambda can work with the flow
const simpleResponse = (intentRequest, callback) => {
  const { slots } = intentRequest.currentIntent;
  const $msg = `Thank you for using the lambda function.
  You submitted the following values AccountType:${slots.AccountType} 
  pinNumber ${slots.PinNumber}. Now it's time to make it actually do something!`;
  callback(close({}, 'Fulfilled', {
    contentType: 'PlainText',
    content: $msg,
  }));
};

// Called when the user specifies an intent for this skill.
const dispatch = (intentRequest, callback) => {
  console.log(JSON.stringify(intentRequest, null, 2));
  console.log(`dispatch userId=${intentRequest.userId}, intentName=${intentRequest.currentIntent.name}`);
  const intentName = intentRequest.currentIntent.name;

  if (intentName === 'GetBalanceCheck') {
    return simpleResponse(intentRequest, callback);
    // return balanceIntentError(intentRequest, callback);
    // return balanceIntent(intentRequest, callback);
  }
  return {};
};

const loggingCallback = (response, originalCallback) => {
  console.log('lambda response:\n', JSON.stringify(response, null, 2));
  originalCallback(null, response);
};

// The handler function is the one that gets called by lambda as it is invoked
exports.handler = (event, context, callback) => {
  try {
    console.log(`event.bot.name=${event.bot.name}`);
    dispatch(event, response => loggingCallback(response, callback));
  } catch (err) {
    callback(err);
  }
};


// --------------- Helpers that build all of the responses -----------------------
// continue dialog with the customer, expressing that the user will select another intent after
// she hears this response
const nextIntent = (sessionAttributes, message) => {
  console.log(`nextIntent:  ${JSON.stringify(message)}`);
  return {
    sessionAttributes,
    dialogAction: {
      type: 'ElicitIntent',
      message,
    },
  };
};

const elicitSlot = (sessionAttributes, intentName, slots, slotToElicit, message) => ({
  sessionAttributes,
  dialogAction: {
    type: 'ElicitSlot',
    intentName,
    slots,
    slotToElicit,
    message,
  },
});


const confirmIntent = (sessionAttributes, intentName, slots, message) => ({
  sessionAttributes,
  dialogAction: {
    type: 'ConfirmIntent',
    intentName,
    slots,
    message,
  },
});


const close = (sessionAttributes, fulfillmentState, message) => ({
  sessionAttributes,
  dialogAction: {
    type: 'Close',
    fulfillmentState,
    message,
  },
});

const delegate = (sessionAttributes, slots) => ({
  sessionAttributes,
  dialogAction: {
    type: 'Delegate',
    slots,
  },
});
```



