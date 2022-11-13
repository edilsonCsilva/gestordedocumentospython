const crypto = require('crypto')
const axios = require('axios')

const generate = function(){
    return crypto.randomBytes(20).toString('hex')
}

const request =  function (url,method,data){
    return axios({url,method,data})
}
    
const base_url ='http://127.0.0.1:5080'
test('Api esta Online', async () => {
    const response =  await request(base_url,'get')

    expect(response.status).toBe(200);
});