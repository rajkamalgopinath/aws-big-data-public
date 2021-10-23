var AWS = require("aws-sdk");
AWS.config.update({region: 'us-east-1' });

var fh = new AWS.Firehose();

exports.handler = function(event, context){

fh.putRecord(
{
    DeliveryStreamName:'raj-delivery-stream-1', 
    Record: {Data: new Buffer(JSON.stringify({deviceid:'d1', temp: 100})) }
    
}, 
function(err, data) {
  if (err) console.log(err, err.stack); // an error occurred
  else     console.log(data);           // successful response
  context.done(err, data)
});

}