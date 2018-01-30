Link to refer :- https://github.com/jupyter/kernel_gateway_demos/blob/master/scotch_demo/notebooks/scotch_api_python.ipynb  
  
Installing Kernel Gateway for API  
pip install jupyter_kernel_gateway  
jupyter kernelgateway --generate-config  
  
Hosted at port 8889  
Jupyter kernelgateway --KernelGatewayApp.api='kernel_gateway.notebook_http' 
--KernelGatewayApp.seed_uri='C:/Users/A661249/Documents/Project/Reasoning/Predict_The_Cause_API.ipynb'  
  
Hosted at port 8890  
Jupyter kernelgateway --KernelGatewayApp.api='kernel_gateway.notebook_http'
--KernelGatewayApp.seed_uri='C:/Users/A661249/Documents/Project/Reasoning/EventDataAPI.ipynb'  
  
Postman :-  
1.To check application  
Post URL :- http://localhost:8889/Predict_The_Causes    
Body:    
{"timestamp":"2012-01-01 00:33:20"}  
Header = Content-Type = application/json  
  
2. To check Only EventDataAPI  
Post URL :- http://localhost:8890/Get_Data  
Body:  
{"timestamp":"2012-01-01 00:33:20"}  
Header = Content-Type = application/json  
  
3. To check Only Predict_The_Cause_API  
Post URL :- http://localhost:8889/Predict  
Body:  
{"Input": [29.17471568, 29.76405684, 30.84482463, 30.32339391, 29.73329031, 30.04066685, 30.74194659, 30.25092148, 29.648114899999996, 29.78398576, 29.44049608, 30.42494734, 29.8298252, 30.07808228, 29.77551232, 29.27337296, 30.40738712, 29.9320071, 30.26984677, 29.44525899, 30.36537878, 30.77201624, 29.83361093, 29.72099028, 28.65408974, 30.13280888, 30.25031467, 29.96891504, 29.48724756, 29.61136307, 29.98093748, 30.46535166, 29.85213395, 29.45589858, 30.25467641, 30.55215087, 29.4992104, 29.87112633, 29.80089984, 29.20870178, 29.74376399, 30.33484934, 30.8231989, 29.430069300000003, 29.86908799, 29.96191701, 29.91692151, 30.177001500000003, 30.64518861, 29.96955381, 30.07169073, 30.36864912, 30.73827504, 29.7723913, 29.68167733, 29.93330285, 28.69097815, 29.82367845, 30.68329403, 29.607483000000002, 30.32338649, 30.51421384, 30.30619298, 30.07369326, 29.92504874, 30.35590828, 30.66255272, 30.26004771, 30.08813001, 29.88002286, 27.0, 26.0, 25.0, 25.0, 27.0, 27.0, 26.0, 25.0, 25.0, 27.0, 21.64596788, 21.37790812, 22.71692561, 22.27252918, 22.98197372, 21.69462767, 21.52714713, 21.51106944, 22.72719788, 22.71152529, 21.66094746, 21.61024023, 21.62752464, 21.97324834, 22.37603146, 21.33221417, 22.24078944, 22.06440349, 21.78198183, 23.01542598]}  
  
Header = Content-Type = application/json  
 
