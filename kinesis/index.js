'use strict';
console.log('Loading function');


exports.handler = async (event, context, callback) => {
    /* Process the list of records and transform them */
    const output = event.records.map((record) => {
        /* This transformation is the "identity" transformation, the data is left intact */
        let entry = (new Buffer(record.data, 'base64')).toString('utf8');
        let result = entry + "|processed\n";
        const payload = (new Buffer(result, 'utf8')).toString('base64');
        return {
        recordId: record.recordId,
        result: 'Ok',
        data: payload,
        }
        });
        
    console.log(`Processing completed.  Successful records ${output.length}.`);
    callback(null, {records: output})
    //return { records: output };
};
