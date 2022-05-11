const testDict = {'EI':0, 'NS':0, 'TF':0, 'PJ':0}

const testList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

localStorage.setItem('testDict', JSON.stringify(testDict));

const retrievedDict = localStorage.getItem('testDict');

console.log('retrievedDict: ', JSON.parse(retrievedDict));