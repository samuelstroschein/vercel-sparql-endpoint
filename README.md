# Host your own SPARQL Endpoint on your website  

The code is a serverless function which could theoretically run through any platform (AWS, Google Cloud etc.) but for ease of use everything is configured for vercel. So here is a step by step tutorial:  

1. Host your website with [Vercel](https://vercel.com/). Don't worry you just give access to your GitHub Repo and within 1 minute your website is live!
2. Pickle your ontology.ttl with the ttl_to_pickle.py script. 
3. Add all files contained in 'root folder of your website' to the root folder of your website hosted with vercel. 
4. Replace your ontology here in the api folder with the pickled ontology you got from running the script.
5. Push and Done!  

Your endpoint is now running under {yourDomain.vercel.com}/api/sparql

### Limitations
1. Vercel only allows for a maximum of 10 Seconds execution time on the free tier. Therefore, the ttl file is pickled (which makes the function faster) but complicated/slow queries could timeout. If a function times out you will get a CORS error and need yo adjust your query.
2. Only RDFlib supported queries can be executed.


### License
You can do whatever you want with the code but you have to provide credit when you are using the code for a course at the Vrije Universiteit Amsterdam. Just link to this repo and give as authors Samuel Stroschein, Satiga Godrie, Tim Brandt Corstius and Azra Cinar! :)
