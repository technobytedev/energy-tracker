import webview
import os
import sqlite3
import base64
import uuid

class Api:

	def delete_appliance_canvas(self, canvas_id):
		try:
			# Connect to the SQLite database
			connection = sqlite3.connect('ecoenergy.db')
			cursor = connection.cursor()
				
			# Insert the appliance and image path into the database
			query = "DELETE FROM canvas WHERE id = ?;"
			cursor.execute(query, (canvas_id,))
			connection.commit()  # Commit the transaction
				
			return {'message': 'Removed successfully.'}
			
		except sqlite3.Error as e:
			return {'error': 'Error occured please try again'}
			
		finally:
			if cursor:
				cursor.close()
			if connection:
				connection.close()


	def update_appliance_canvas(self, simulation_id ,room_id, appliance_id, from_room, canvas_id):
		try:
			connection = sqlite3.connect('ecoenergy.db')
			cursor = connection.cursor()

			restricted_appliance_id_1 = ['91', '92', '93', '94']
			restricted_appliance_id_2 = ['77', '78', '79', '80']

			restricted_rooms_id_1 = [
	            'cont1_bedroom2', 'cont1_bedroom3',
	            'cont1_greatroom', 'cont1_masterbedroom',
	            'cont1_bathroom', 'cont1_master_bathroom',
	            'duplex2_bedroom1', 'duplex2_bedroom3',
	            'duplex2_bedroom1', 'duplex2_bedroom2',
	            'duplex2_bedroom3', 'duplex2_bathroom1',
	            'duplex2_bathroom2', 'duplex3_bedroom',
	            'bungalow1_bedroom1', 'bungalow1_bedroom2',
	            'bungalow1_bedroom3', 'cont2_master_bathroom',
	            'cont2_bathroom', 'duplex1_bathroom',
	            'duplex1_bedroom1', 'duplex1_bedroom2',
	            'bungalow2_bedroom1',
	            'bungalow2_bedroom2', 'bungalow3_bedroom1',
	            'bungalow3_bedroom2', 'bungalow3_bathroom',
	            'bungalow2_master_bedroom', 'bungalow2_bathroom',
	            'cont2_master_bedroom','bungalow1_bath1', 'bungalow1_bath2'
	       		]

			restricted_rooms_id_2 = [
	            'cont1_greatroom',
	            'cont1_bathroom',
	            'duplex2_bathroom1',
	            'duplex2_bathroom2','cont2_master_bathroom',
	            'cont2_bathroom', 'duplex1_bathroom','bungalow2_bathroom',
	          	'bungalow1_bath1', 'bungalow1_bath2'
	       		]	       		


			if room_id in restricted_rooms_id_1 and appliance_id in restricted_appliance_id_1:
				return {'error': 'Unable to transfer appliance to this room, for safety purposes.'}

			if room_id in restricted_rooms_id_2 and appliance_id in restricted_appliance_id_2:
				return {'error': 'Unable to transfer appliance to this room, for safety purposes.'}			

			# Insert the appliance and image path into the database
			query = "UPDATE canvas SET room_id = ? WHERE id = ?;"
			cursor.execute(query, (room_id, canvas_id))
			connection.commit()  # Commit the transaction
					
			return {'message': 'Transfered successfully.'}
			
		except sqlite3.Error as e:
			return {'error': 'Error occured please try again'}
			
		finally:
			if cursor:
				cursor.close()
			if connection:
				connection.close()


	def add_appliance_canvas(self, simulation_id, room_id, appliance_id):
	    try:
	    	# Connect to the SQLite database
	        connection = sqlite3.connect('ecoenergy.db')
	        cursor = connection.cursor()

	        restricted_appliance_id_1 = ['91', '92', '93', '94']
	        restricted_appliance_id_2 = ['77', '78', '79', '80']

	        restricted_rooms_id_1 = [
	            'cont1_bedroom2', 'cont1_bedroom3',
	            'cont1_greatroom', 'cont1_masterbedroom',
	            'cont1_bathroom', 'cont1_master_bathroom',
	            'duplex2_bedroom1', 'duplex2_bedroom3',
	            'duplex2_bedroom1', 'duplex2_bedroom2',
	            'duplex2_bedroom3', 'duplex2_bathroom1',
	            'duplex2_bathroom2', 'duplex3_bedroom',
	            'bungalow1_bedroom1', 'bungalow1_bedroom2',
	            'bungalow1_bedroom3', 'cont2_master_bathroom',
	            'cont2_bathroom', 'duplex1_bathroom',
	            'duplex1_bedroom1', 'duplex1_bedroom2',
	            'bungalow2_bedroom1',
	            'bungalow2_bedroom2', 'bungalow3_bedroom1',
	            'bungalow3_bedroom2', 'bungalow3_bathroom',
	            'bungalow2_master_bedroom', 'bungalow2_bathroom',
	            'cont2_master_bedroom','bungalow1_bath1', 'bungalow1_bath2','cont3_master_bathroom',
	            'cont3_master_bedroom','cont3_bathroom', 'cont3_bedroom'
	       		]
	       	restricted_rooms_id_2 = [
	            'cont1_greatroom',
	            'cont1_bathroom',
	            'duplex2_bathroom1',
	            'duplex2_bathroom2','cont2_master_bathroom',
	            'cont2_bathroom', 'duplex1_bathroom','bungalow2_bathroom',
	          	'bungalow1_bath1', 'bungalow1_bath2','cont3_master_bathroom',
	          	'cont3_bathroom'
	       		]	  	       		

	       	if room_id in restricted_rooms_id_1 and appliance_id in restricted_appliance_id_1:
	       		return {'error': 'Unable to transfer appliance to this room, for safety purposes.'}
	       	if room_id in restricted_rooms_id_2 and appliance_id in restricted_appliance_id_2:
	       		return {'error': 'Unable to transfer appliance to this room, for safety purposes.'}

	        # Insert the appliance and image path into the database
	        query = "INSERT INTO canvas(simulation_id, room_id, appliance_id) VALUES(?, ?, ?);"
	        cursor.execute(query, (simulation_id, room_id, appliance_id))
	        connection.commit()  # Commit the transaction

	        return {'message': 'Appliance added to room.'}
	    except sqlite3.Error as e:
	    	return {'error': 'Error occurred, please try again'}
	    finally:
	    	if cursor:
	    		cursor.close()
	    	if connection:
	    		connection.close()
	    # except sqlite3.Error as e:
	    # 	return {'error': 'Error occurred, please try again'}

		# finally:
		# 	if cursor:
		# 		cursor.close()
		# 	if connection:
		# 		connection.close()


	def create_room(self, room_name, simulation_id):
		try:
			# Connect to the SQLite database
			connection = sqlite3.connect('ecoenergy.db')
			cursor = connection.cursor()
				
			# Insert the appliance and image path into the database
			query = "INSERT INTO room(name, simulation_id) VALUES(?, ?);"
			cursor.execute(query, (room_name, simulation_id))
			connection.commit()  # Commit the transaction
				
			return {'message': 'Room created successfully.'}
			
		except sqlite3.Error as e:
			return {'error': 'Error occured please try again'}

		finally:
			if cursor:
				cursor.close()
			if connection:
				connection.close()


	def create_simulation(self, name):
		try:
			# Connect to the SQLite database
			connection = sqlite3.connect('ecoenergy.db')
			cursor = connection.cursor()
				
			# Insert the appliance and image path into the database
			query = "INSERT INTO simulation(name) VALUES(?);"
			cursor.execute(query, (name,))
			connection.commit()  # Commit the transaction
			session_id = cursor.lastrowid
				
			return {'message': 'Simulation created successfully.', 'session_id': session_id}
			
		except sqlite3.Error as e:
			return {'error': 'Error occured please try again'}
			
		finally:
			if cursor:
				cursor.close()
			if connection:
				connection.close()

	def upload_image(self, base64_image, appliance, name, watt):
			try:
				# Decode the base64 image
				image_data = base64.b64decode(base64_image)
				image_name = f"{str(uuid.uuid4())}.png"
				
				# Specify the upload folder path
				upload_folder = os.path.join(os.getcwd(), 'assets/uploads')
				
				# Create the folder if it doesn't exist
				if not os.path.exists(upload_folder):
					os.makedirs(upload_folder)
				
				# Full file path for the image
				file_path = os.path.join(upload_folder, image_name)
				
				# Write the image to the folder
				with open(file_path, 'wb') as f:
					f.write(image_data)
				
				# Connect to the SQLite database
				connection = sqlite3.connect('ecoenergy.db')
				cursor = connection.cursor()
				
				# Insert the appliance and image path into the database
				query = "INSERT INTO sub_appliance(appliance_id, image, name, watt) VALUES(?, ?, ?, ?);"
				cursor.execute(query, (appliance, image_name, name, watt))
				connection.commit()  # Commit the transaction
				
				return f'file://{file_path}'
			
			except sqlite3.Error as e:
				return f"Error: {e}"
			
			finally:
				if cursor:
					cursor.close()
				if connection:
					connection.close()

	def appliance_list(self):
		try:
			# Connect to the SQLite database
			connection = sqlite3.connect('ecoenergy.db')
			cursor = connection.cursor()
			
			# Execute the query to get main appliance data
			appliance_query = "SELECT id, name, image FROM appliance;"
			cursor.execute(appliance_query)
			appliances = cursor.fetchall()
			appliance_columns = [description[0] for description in cursor.description]

			result = ""
			for appliance in appliances:
				result += f"""<div style="style="background:#f9f9f9""><br><br><br>
				"""
				appliance_data = {appliance_columns[i]: appliance[i] for i in range(len(appliance))}
				
				# Execute the query to get sub-appliance data for each appliance
				sub_appliance_query = """
				SELECT id, image, watt, name
				FROM sub_appliance
				WHERE appliance_id = ?;
				"""
				cursor.execute(sub_appliance_query, (appliance_data['id'],))
				sub_appliances = cursor.fetchall()
				sub_appliance_columns = [description[0] for description in cursor.description]

				# Generate the main image and dropdown structure
				result += f"""
				<div class="dropdown dropup">
					    <img data-bs-placement="top" title="{appliance_data['name']}" draggable="false" data-is-update="0" id="s{appliance_data['id']}" data-bs-toggle="dropdown" aria-expanded="false" style="width:25px; height:30px; padding:5px;" src="assets/vectors/{appliance_data['image']}" />
    					<ul class="dropdown-menu" style="background:white; z-index: 9999!important; position: absolute; top: -50px;" aria-labelledby="s{appliance_data['id']}">
						<div class="d-flex p-1 text-center">
				"""
				for sub_appliance in sub_appliances:
					sub_appliance_data = {sub_appliance_columns[i]: sub_appliance[i] for i in range(len(sub_appliance))}
					result += f"""
							<div>
								<img data-bs-toggle="tooltip" data-bs-placement="top" title="{sub_appliance_data['name']} - {sub_appliance_data['watt']} W" draggable="true" id="{sub_appliance_data['id']}" style="max-height:35px;margin:4px" src="assets/uploads/{sub_appliance_data['image']}"/>
							</div>
					"""
				result += """
						</div>
					</ul>
				</div>
				"""
				result += f"""</div>
				"""
			
			return {'message': result}
		
		except sqlite3.Error as e:
			return {'message': f"Error: {e}"}
		finally:
			cursor.close()
			connection.close()

	def navbar(self):

		# Connect to the SQLite database (it will create the file if it doesn't exist)
		connection = sqlite3.connect('ecoenergy.db')
		cursor = connection.cursor()
			
		# Execute the query
		cursor.execute("SELECT * FROM simulation ORDER BY name;")
		rows = cursor.fetchall()  # Fetch all rows from the query result
		columns = [description[0] for description in cursor.description]  # Get column names

		# Return the fetched data as a string (for simplicity)

		r = ""

		simulations = ""

		for row in rows:
			row_data = {columns[i]: row[i] for i in range(len(row))}  # Create dict of column names and row values
			simulations += f"""
						 <li><p onclick="setID('{row_data['name']}', '{row_data['id']}');" class="text-white" >{row_data['name']}</p></li>
						"""
		r += """
				<div class="nav-item dropdown">
						<a style="color:black!important" class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
							List of House
						</a>
						<ul class="dropdown-menu p-2 text-white" aria-labelledby="navbarDropdownMenuLink" style="background:gray;width:230px!important">
						"""
		r +=   simulations

		r += """
						</ul>
					</div>
		"""


		return {'message': r}
	# def navbar(self):

	# 	# Connect to the SQLite database (it will create the file if it doesn't exist)
	# 	connection = sqlite3.connect('ecoenergy.db')
	# 	cursor = connection.cursor()
			
	# 	# Execute the query
	# 	cursor.execute("SELECT * FROM simulation ORDER BY name;")
	# 	rows = cursor.fetchall()  # Fetch all rows from the query result
	# 	columns = [description[0] for description in cursor.description]  # Get column names

	# 	# Return the fetched data as a string (for simplicity)

	# 	r = ""

	# 	simulations = ""

	# 	for row in rows:
	# 		row_data = {columns[i]: row[i] for i in range(len(row))}  # Create dict of column names and row values
	# 		simulations += f"""
	# 					 <li><p onclick="setID('{row_data['name']}', '{row_data['id']}');" class="text-white" >{row_data['name']}</p></li>
	# 					"""
	# 	r += """<div class="container-fluid">
			
	# 		<div >
	# 			<button class="navbar-toggler text-white" style="color:white" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
	# 			<span class="navbar-toggler-icon text-white" style="color:white"></span>
	# 			</button>

	# 		</div>
			
	# 		<div class="collapse navbar-collapse" id="navbarNavDropdown">
	# 			<ul class="navbar-nav text-white">
	# 				<li class="nav-item">
	# 					<a class="nav-link active" aria-current="page" href="index.html">Home</a>
	# 				</li>

				

	# 				<li class="nav-item">
	# 					<span class="nav-link" onclick="showComparative();" >Comparative Analysis</span>
	# 				</li>

	# 				<li class="nav-item">
	# 					<span class="nav-link" onclick="showTarget();" >Target Consumption</span>
	# 				</li>

	# 				<li class="nav-item dropdown">
	# 					<a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
	# 						List of House
	# 					</a>
	# 					<ul class="dropdown-menu p-2 text-white" aria-labelledby="navbarDropdownMenuLink" style="background:#CE3A00;width:230px!important">
	# 					"""
	# 	r +=   simulations

	# 	r += """
	# 					</ul>
	# 				</li>
	# 			</ul>
	# 		</div>


	# 		<div class="row">
	# 		<div class="col-6">
			
	# 		</div>
	# 		<div class="col-6">
				
	# 		</div>
	# 		</div>
			
	# 		 <a class="navbar-brand text-white" href="index.html">Eco Energy Tracker</a>

	# 	</div>"""


	# 	return {'message': r}


	def fetch_appliance(self):
		try:
			# Connect to the SQLite database (it will create the file if it doesn't exist)
			connection = sqlite3.connect('ecoenergy.db')
			cursor = connection.cursor()
			
			# Execute the query
			cursor.execute("SELECT * FROM sub_appliance;")
			rows = cursor.fetchall()  # Fetch all rows from the query result
			columns = [description[0] for description in cursor.description]  # Get column names

			# Return the fetched data as a string (for simplicity)
			result = ""
			for row in rows:
				row_data = {columns[i]: row[i] for i in range(len(row))}  # Create dict of column names and row values
				result += f"""<tr>
								<td>{row_data['id']} - {row_data['appliance_id']}</td>
								<td>{row_data['name']}</td>
								<td>{row_data['watt']}</td>
								<td> <img src="assets/uploads/{row_data['image']}" style="width:60px" />  </td>
							</tr>"""
	  
			return {'message': result}
		
		except sqlite3.Error as e:
			return {'message': f"Error: {e}"}
		finally:
			cursor.close()
			connection.close()

	def fetch_room(self, simulation_id):
		try:
			# Connect to the SQLite database
			connection = sqlite3.connect('ecoenergy.db')
			cursor = connection.cursor()
			
			# Query to fetch room and canvas details
			query = """SELECT room.id AS roomId, room.name AS roomName, sub_appliance.image AS applianceImage, 
			sub_appliance.id AS applianceImageId, sub_appliance.name AS applianceName, canvas.id AS canvasRow, 
			sub_appliance.watt AS watt
			FROM canvas 
			 JOIN room ON room.id = canvas.room_id
			JOIN sub_appliance ON sub_appliance.id = canvas.appliance_id
			WHERE canvas.simulation_id = ?;"""

			cursor.execute(query, (simulation_id,))
			rows = cursor.fetchall()  # Fetch all rows from the query result

			columns = [description[0] for description in cursor.description]  # Get column names

			# Group images by roomId
			grouped_data = {}
			for row in rows:
				row_data = {columns[i]: row[i] for i in range(len(row))}
				room_id = row_data['roomId']
				canvas_id = row_data['canvasRow']  # Fetch the canvas.id
				watt = row_data['watt'] 
				
				if room_id not in grouped_data:
					grouped_data[room_id] = {
						'roomName': row_data['roomName'],
						'canvasRow': canvas_id,
						'images': [],
						'watt': watt

					}
				# Append image, image_id, and canvas_id to the list of images
				grouped_data[room_id]['images'].append((row_data['applianceImage'], row_data['applianceImageId'], canvas_id, watt, row_data['applianceName']))

			if(simulation_id == '85'):
				# Map HTML IDs to room IDs
				room_id_map = {
					'duplex2_bedroom1': 'duplex2_bedroom1',
					'duplex2_bedroom2': 'duplex2_bedroom2',
					'duplex2_bedroom3': 'duplex2_bedroom3',
					'duplex2_kitchen': 'duplex2_kitchen',
					'duplex2_laundry': 'duplex2_laundry',
					'duplex2_dining': 'duplex2_dining',
					'duplex2_bathroom1': 'duplex2_bathroom1',
					'duplex2_living': 'duplex2_living',
					'duplex2_porch': 'duplex2_porch',
					'duplex2_bathroom2': 'duplex2_bathroom2'
					}

				# Generate HTML

				result = """
				<img src='assets/blueprints/duplex2.png' usemap="#image-map" style="width:auto; height:auto"><br>
				<map name="image-map" style="display:none">
				    <area id="duplex2_bedroom1" class="droptarget" data-bs-toggle="modal" data-bs-target="#duplex2_bedroom1Modal" alt="bedroom1" title="Click to View Bedroom 1" coords="17,424,223,637" shape="rect">
				    <area id="duplex2_bedroom2" class="droptarget" data-bs-toggle="modal" data-bs-target="#duplex2_bedroom2Modal" alt="bedroom2" title="Click to View Bedroom 2" coords="211,14,379,225" shape="rect">
				    <area id="duplex2_bedroom3" class="droptarget" data-bs-toggle="modal" data-bs-target="#duplex2_bedroom3Modal" alt="bedroom3" title="Click to View Bedroom 3" coords="16,16,184,227" shape="rect">
				    <area id="duplex2_kitchen" class="droptarget" data-bs-toggle="modal" data-bs-target="#duplex2_kitchenModal" alt="kitchen" title="Click to View Kitchen" coords="399,13,589,192" shape="rect">
				    <area id="duplex2_laundry" class="droptarget" data-bs-toggle="modal" data-bs-target="#duplex2_laundryModal" alt="laundry" title="Click to View Laundry" coords="13,249,110,413" shape="rect">
				    <area id="duplex2_dining" class="droptarget" data-bs-toggle="modal" data-bs-target="#duplex2_diningModal" alt="dining" title="Click to View Dining" coords="400,205,591,349" shape="rect">
				    <area id="duplex2_bathroom1" class="droptarget" data-bs-toggle="modal" data-bs-target="#duplex2_bathroom1Modal" alt="bathroom1" title="Click to View Bathroom 1" coords="243,319,324,462" shape="rect">
				    <area id="duplex2_living" class="droptarget" data-bs-toggle="modal" data-bs-target="#duplex2_livingModal" alt="living" title="Click to View Living Room" coords="349,373,588,643" shape="rect">
				    <area id="duplex2_porch" class="droptarget" data-bs-toggle="modal" data-bs-target="#duplex2_porchModal" alt="porch" title="Click to View Porch" coords="608,363,680,440" shape="rect">
				    <area id="duplex2_bathroom2" class="droptarget" data-bs-toggle="modal" data-bs-target="#duplex2_bathroom2Modal" alt="bathroom2" title="Click to View Bathroom 2" coords="245,480,325,634" shape="rect">
				</map>

				<!-- Modal for Duplex2 Bedroom 1 -->
				<div class="modal fade" id="duplex2_bedroom1Modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Bedroom 1</h5>
				              <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {duplex2_bedroom1}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Duplex2 Bedroom 2 -->
				<div class="modal fade" id="duplex2_bedroom2Modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Bedroom 2</h5>
				               <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {duplex2_bedroom2}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Duplex2 Bedroom 3 -->
				<div class="modal fade" id="duplex2_bedroom3Modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Bedroom 3</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {duplex2_bedroom3}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Duplex2 Kitchen -->
				<div class="modal fade" id="duplex2_kitchenModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Kitchen</h5>
					                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {duplex2_kitchen}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Duplex2 Laundry -->
				<div class="modal fade" id="duplex2_laundryModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Laundry</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {duplex2_laundry}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Duplex2 Dining -->
				<div class="modal fade" id="duplex2_diningModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Dining Room</h5>
								<div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {duplex2_dining}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Duplex2 Bathroom 1 -->
				<div class="modal fade" id="duplex2_bathroom1Modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Bathroom 1</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {duplex2_bathroom1}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Duplex2 Living Room -->
				<div class="modal fade" id="duplex2_livingModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Living Room</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {duplex2_living}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Duplex2 Porch -->
				<div class="modal fade" id="duplex2_porchModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Porch</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {duplex2_porch}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Duplex2 Bathroom 2 -->
				<div class="modal fade" id="duplex2_bathroom2Modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Bathroom 2</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {duplex2_bathroom2}
				            </div>
				        </div>
				    </div>
				</div>

				"""
			if(simulation_id == '84'):
				# Map HTML IDs to room IDs
				room_id_map = {
					'cont1_patio': 'cont1_patio',
					'cont1_garage': 'cont1_garage',
					'cont1_pantry': 'cont1_pantry',
					'cont1_kitchen': 'cont1_kitchen',
					'cont1_bedroom2': 'cont1_bedroom2',
					'cont1_bedroom3': 'cont1_bedroom3',
					'cont1_greatroom': 'cont1_greatroom',
					'cont1_masterbedroom': 'cont1_masterbedroom',
					'cont1_bathroom': 'cont1_bathroom',
					'cont1_master_bathroom': 'cont1_master_bathroom'
				}
				result = """
				<img src='assets/blueprints/contemporary1.png' usemap="#image-map" style="width:auto; height:auto"><br>

				<map name="image-map" style="display:none">
				    <area id="cont1_patio" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont1_patioModal" alt="patio" title="Click to View Patio" coords="234,27,438,163" shape="rect">
				    <area id="cont1_garage" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont1_garageModal" alt="garage" title="Click to View Garage" coords="35,70,213,356" shape="rect">
				    <area id="cont1_pantry" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont1_pantryModal" alt="pantry" title="Click to View Pantry" coords="233,297,318,248" shape="rect">
				    <area id="cont1_kitchen" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont1_kitchenModal" alt="kitchen" title="Click to View Kitchen" coords="306,171,428,368" shape="rect">
				    <area id="cont1_bedroom2" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont1_bedroom2Modal" alt="bedroom2" title="Click to View Bedroom 2" coords="471,171,598,326" shape="rect">
				    <area id="cont1_bedroom3" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont1_bedroom3Modal" alt="bedroom3" title="Click to View Bedroom 3" coords="612,173,780,293" shape="rect">
				    <area id="cont1_greatroom" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont1_greatroomModal" alt="greatroom" title="Click to View Great Room" coords="305,369,497,596" shape="rect">
				    <area id="cont1_masterbedroom" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont1_masterbedroomModal" alt="masterbedroom" title="Click to View Master Bedroom" coords="558,475,749,656" shape="rect">
				    <area id="cont1_bathroom" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont1_bathroomModal" alt="bathroom" title="Click to View Bathroom" coords="763,328,838,449" shape="rect">
				    <area id="cont1_master_bathroom" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont1_master_bathroomModal" alt="master_bathroom" title="Click to View Master Bathroom" coords="763,461,837,587" shape="rect">
				</map>

				<!-- Modal for Cont1 Patio -->
				<div class="modal fade" id="cont1_patioModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Patio</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {cont1_patio}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Cont1 Garage -->
				<div class="modal fade" id="cont1_garageModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Garage</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {cont1_garage}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Cont1 Pantry -->
				<div class="modal fade" id="cont1_pantryModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Pantry</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {cont1_pantry}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Cont1 Kitchen -->
				<div class="modal fade" id="cont1_kitchenModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Kitchen</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {cont1_kitchen}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Cont1 Bedroom 2 -->
				<div class="modal fade" id="cont1_bedroom2Modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Bedroom 2</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {cont1_bedroom2}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Cont1 Bedroom 3 -->
				<div class="modal fade" id="cont1_bedroom3Modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Bedroom 3</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {cont1_bedroom3}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Cont1 Great Room -->
				<div class="modal fade" id="cont1_greatroomModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Great Room</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {cont1_greatroom}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Cont1 Master Bedroom -->
				<div class="modal fade" id="cont1_masterbedroomModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Master Bedroom</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {cont1_masterbedroom}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Cont1 Bathroom -->
				<div class="modal fade" id="cont1_bathroomModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Bathroom</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {cont1_bathroom}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Cont1 Master Bathroom -->
				<div class="modal fade" id="cont1_master_bathroomModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Master Bathroom</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {cont1_master_bathroom}
				            </div>
				        </div>
				    </div>
				</div>

				"""

			if(simulation_id == '86'):
				# Map HTML IDs to room IDs Duplex 3
				room_id_map = {
					'duplex3_porch1': 'duplex3_porch1',
					'duplex3_porch2': 'duplex3_porch2',
					'duplex3_bedroom': 'duplex3_bedroom',
					'duplex3_kitchen': 'duplex3_kitchen',
					'duplex3_dining': 'duplex3_dining',
					'duplex3_living': 'duplex3_living'
				}
				result = """
			<img src='assets/blueprints/duplex3.png' usemap="#image-map" style="width:auto; height:auto"><br>
				<map name="image-map" style="display:none">
				    <area id="duplex3_porch1" class="droptarget" data-bs-toggle="modal" data-bs-target="#duplex3_porch1Modal" alt="dining-kitchen1" title="Click to View Appliances" coords="30,895,243,965" shape="rect">
				    <area id="duplex3_porch2" class="droptarget" data-bs-toggle="modal" data-bs-target="#duplex3_porch2Modal" alt="dining-kitchen1" title="Click to View Appliances" coords="40,6,277,91" shape="rect">
				    <area id="duplex3_bedroom" class="droptarget" data-bs-toggle="modal" data-bs-target="#duplex3_bedroomModal" alt="dining-kitchen1" title="Click to View Appliances" coords="40,118,283,318" shape="rect">
				    <area id="duplex3_kitchen" class="droptarget" data-bs-toggle="modal" data-bs-target="#duplex3_kitchenModal" alt="dining-kitchen1" title="Click to View Appliances" coords="27,446,152,615" shape="rect">
				    <area id="duplex3_dining" class="droptarget" data-bs-toggle="modal" data-bs-target="#duplex3_diningModal" alt="dining-kitchen1" title="Click to View Appliances" coords="167,434,399,619" shape="rect">
				    <area id="duplex3_living" class="droptarget" data-bs-toggle="modal" data-bs-target="#duplex3_livingModal" alt="dining-kitchen1" title="Click to View Appliances" coords="41,627,401,876" shape="rect">
				</map>

				<div class="modal fade" id="duplex3_porch1Modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Porch 1</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {duplex3_porch1}
				            </div>
				        </div>
				    </div>
				</div>
				<div class="modal fade" id="duplex3_porch2Modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
			    <div class="modal-dialog modal-dialog-centered" role="document">
			        <div class="modal-content">
			            <div class="modal-header">
			                <h5 class="modal-title" id="exampleModalLabel">Porch 2</h5>
			                <div style="width:100px" class="row">
			                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
			                    <div class="col p-2">
			                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
			                    </div>
			                </div>
			            </div>
			            <div class="modal-body d-flex">
			                {duplex3_porch2}
			            </div>
			        </div>
			    </div>
			</div>

			<div class="modal fade" id="duplex3_bedroomModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
			    <div class="modal-dialog modal-dialog-centered" role="document">
			        <div class="modal-content">
			            <div class="modal-header">
			                <h5 class="modal-title" id="exampleModalLabel">Bedroom</h5>
			                <div style="width:100px" class="row">
			                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
			                    <div class="col p-2">
			                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
			                    </div>
			                </div>
			            </div>
			            <div class="modal-body d-flex">
			                {duplex3_bedroom}
			            </div>
			        </div>
			    </div>
			</div>

			<div class="modal fade" id="duplex3_kitchenModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
			    <div class="modal-dialog modal-dialog-centered" role="document">
			        <div class="modal-content">
			            <div class="modal-header">
			                <h5 class="modal-title" id="exampleModalLabel">Kitchen</h5>
			                <div style="width:100px" class="row">
			                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
			                    <div class="col p-2">
			                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
			                    </div>
			                </div>
			            </div>
			            <div class="modal-body d-flex">
			                {duplex3_kitchen}
			            </div>
			        </div>
			    </div>
			</div>

			<div class="modal fade" id="duplex3_diningModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
			    <div class="modal-dialog modal-dialog-centered" role="document">
			        <div class="modal-content">
			            <div class="modal-header">
			                <h5 class="modal-title" id="exampleModalLabel">Dining</h5>
			                <div style="width:100px" class="row">
			                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
			                    <div class="col p-2">
			                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
			                    </div>
			                </div>
			            </div>
			            <div class="modal-body d-flex">
			                {duplex3_dining}
			            </div>
			        </div>
			    </div>
			</div>

			<div class="modal fade" id="duplex3_livingModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
			    <div class="modal-dialog modal-dialog-centered" role="document">
			        <div class="modal-content">
			            <div class="modal-header">
			                <h5 class="modal-title" id="exampleModalLabel">Living Room</h5>
			                <div style="width:100px" class="row">
			                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
			                    <div class="col p-2">
			                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
			                    </div>
			                </div>
			            </div>
			            <div class="modal-body d-flex">
			                {duplex3_living}
			            </div>
			        </div>
			    </div>
			</div>

				"""

			if(simulation_id == '87'):
				# Map HTML IDs to room IDs Bungalow 1
				room_id_map = {
					'bungalow1_laundry': 'bungalow1_laundry',
					'bungalow1_dining_kitchen': 'bungalow1_dining_kitchen',

					'bungalow1_bedroom1': 'bungalow1_bedroom1',
					'bungalow1_bedroom2': 'bungalow1_bedroom2',
					'bungalow1_bedroom3': 'bungalow1_bedroom3',

					'bungalow1_living_room': 'bungalow1_living_room',

					'bungalow1_bath1': 'bungalow1_bath1',
					'bungalow1_bath2': 'bungalow1_bath2',

					'bungalow1_garage': 'bungalow1_garage',

					'bungalow1_porch': 'bungalow1_porch'

				}
				result = """
				<img src='assets/blueprints/bungalow1.png' usemap="#image-map" style="width:auto; height:auto"><br>
				<map name="image-map" style="display:none">
				    <area id="bungalow1_dining_kitchen" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow1_dining_kitchenModal" alt="dining-kitchen1" title="Click to View Appliances" coords="230,303,60,194" shape="rect">
				    <area id="bungalow1_bedroom1" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow1_bedroom1Modal" alt="dining-kitchen1" title="Click to View Appliances" coords="428,243,267,144" shape="rect">
				    <area id="bungalow1_bedroom2" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow1_bedroom2Modal" alt="dining-kitchen1" title="Click to View Appliances" coords="616,241,483,145" shape="rect">
				    <area id="bungalow1_bedroom3" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow1_bedroom3Modal" alt="dining-kitchen1" title="Click to View Appliances" coords="605,616,497,529" shape="rect">
				    <area id="bungalow1_laundry" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow1_laundryModal" alt="dining-kitchen1" title="Click to View Appliances" coords="238,98,53,46" shape="rect">
				    <area id="bungalow1_living_room" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow1_living_roomModal" alt="dining-kitchen1" title="Click to View Appliances" coords="431,506,279,311" shape="rect">
				    <area id="bungalow1_bath1" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow1_bath1Modal" alt="dining-kitchen1" title="Click to View Appliances" coords="663,354,565,306" shape="rect">
				    <area id="bungalow1_bath2" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow1_bath2Modal" alt="dining-kitchen1" title="Click to View Appliances" coords="662,445,565,406" shape="rect">
				    <area id="bungalow1_garage" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow1_garageModal" alt="dining-kitchen1" title="Click to View Appliances" coords="197,572,96,456" shape="rect">
				    <area id="bungalow1_porch" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow1_porchModal" alt="dining-kitchen1" title="Click to View Appliances" coords="398,634,297,578" shape="rect">
				</map>

				<!-- Bootstrap Modal for Dining/Kitchen -->
				<div class="modal fade" id="bungalow1_dining_kitchenModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Dining/Kitchen</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {bungalow1_dining_kitchen}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Bedroom 1 -->
				<div class="modal fade" id="bungalow1_bedroom1Modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Bedroom 1</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {bungalow1_bedroom1}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Bedroom 2 -->
				<div class="modal fade" id="bungalow1_bedroom2Modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Bedroom 2</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {bungalow1_bedroom2}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Bedroom 3 -->
				<div class="modal fade" id="bungalow1_bedroom3Modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Bedroom 3</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {bungalow1_bedroom3}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Laundry -->
				<div class="modal fade" id="bungalow1_laundryModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Laundry</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {bungalow1_laundry}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Living Room -->
				<div class="modal fade" id="bungalow1_living_roomModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Living Room</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {bungalow1_living_room}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Bath 1 -->
				<div class="modal fade" id="bungalow1_bath1Modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Bath 1</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {bungalow1_bath1}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Bath 2 -->
				<div class="modal fade" id="bungalow1_bath2Modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Bath 2</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {bungalow1_bath2}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Garage -->
				<div class="modal fade" id="bungalow1_garageModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Garage</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {bungalow1_garage}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Porch -->
				<div class="modal fade" id="bungalow1_porchModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Porch</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {bungalow1_porch}
				            </div>
				        </div>
				    </div>
				</div>
	
				"""

			if(simulation_id == '88'):
				# Map HTML IDs to room IDs Contemporary 2
				room_id_map = {
					'cont2_mudroom': 'cont2_mudroom',
					'cont2_kitchen': 'cont2_kitchen',
					'cont2_bed2': 'cont2_bed2',

					'cont2_mech': 'cont2_mech',
					'cont2_master_bathroom': 'cont2_master_bathroom',
					'cont2_master_bedroom': 'cont2_master_bedroom',

					'cont2_wic': 'cont2_wic',

					'cont2_dining': 'cont2_dining',
					'cont2_living': 'cont2_living',
					'cont2_covered_porch': 'cont2_covered_porch',

					'cont2_bathroom': 'cont2_bathroom',
					'cont2_bed3': 'cont2_bed3',
					'cont2_pantry':'cont2_pantry'
				}
				result = """
				<img src='assets/blueprints/contemporary2.png' usemap="#image-map" style="width:auto; height:auto"><br>
				<map name="image-map" style="display:none">
				    <area id="cont2_mudroom" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont2_mudroomModal" alt="mudroom" title="Click to View Mud Room" coords="79,52,364,162" shape="rect">
				    <area id="cont2_kitchen" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont2_kitchenModal" alt="kitchen" title="Click to View Kitchen" coords="385,82,586,248" shape="rect">
				    <area id="cont2_bed2" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont2_bed2Modal" alt="bed2" title="Click to View Bedroom 2" coords="685,53,888,246" shape="rect">
				    <area id="cont2_mech" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont2_mechModal" alt="mech" title="Click to View Mechanical" coords="73,173,234,225" shape="rect">
				    <area id="cont2_master_bathroom" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont2_master_bathroomModal" alt="master_bathroom" title="Click to View Master Bathroom" coords="76,237,237,391" shape="rect">
				    <area id="cont2_wic" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont2_wicModal" alt="wic" title="Click to View Walk-In Closet" coords="249,251,367,387" shape="rect">
				    <area id="cont2_dining" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont2_diningModal" alt="dining" title="Click to View Dining Room" coords="386,255,667,441" shape="rect">
				    <area id="cont2_living" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont2_livingModal" alt="living" title="Click to View Living Room" coords="379,444,665,662" shape="rect">
				    <area id="cont2_covered_porch" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont2_covered_porchModal" alt="covered_porch" title="Click to View Covered Porch" coords="68,684,898,802" shape="rect">
				    <area id="cont2_bathroom" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont2_bathroomModal" alt="bathroom" title="Click to View Bathroom" coords="741,293,890,407" shape="rect">
				  	<area id="cont2_master_bedroom" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont2_master_bedroomModal" alt="master_bathroom" title="Click to View Master Bathroom" coords="34,291,210,432" shape="rect">  
				    <area id="cont2_bed3" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont2_bed3Modal" alt="bed3" title="Click to View Bedroom 3" coords="690,438,890,636" shape="rect">
				    <area id="cont2_pantry" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont2_pantryModal" alt="bed3" title="Click to View Pantry" coords="594,50,673,130" shape="rect">


				</map>



				<div class="modal fade" id="cont2_pantryModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Pantry</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {cont2_pantry}
				            </div>
				        </div>
				    </div>
				</div>


				<div class="modal fade" id="cont2_master_bedroomModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Masters Bedroom</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {cont2_master_bedroom}
				            </div>
				        </div>
				    </div>
				</div>
				<!-- Modal for Cont2 Mudroom -->
				<div class="modal fade" id="cont2_mudroomModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Mud Room</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {cont2_mudroom}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Cont2 Kitchen -->
				<div class="modal fade" id="cont2_kitchenModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Kitchen</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {cont2_kitchen}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Cont2 Bedroom 2 -->
				<div class="modal fade" id="cont2_bed2Modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Bedroom 2</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {cont2_bed2}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Cont2 Mechanical -->
				<div class="modal fade" id="cont2_mechModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Mechanical</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {cont2_mech}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Cont2 Master Bathroom -->
				<div class="modal fade" id="cont2_master_bathroomModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Master Bathroom</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {cont2_master_bathroom}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Cont2 Master Bathroom -->
				<div class="modal fade" id="cont2_wicModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Walkin Closet</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {cont2_wic}
				            </div>
				        </div>
				    </div>
				</div>

								<!-- Modal for Cont2 Master Bathroom -->
				<div class="modal fade" id="cont2_diningModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Dining</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {cont2_dining}
				            </div>
				        </div>
				    </div>
				</div>
												<!-- Modal for Cont2 Master Bathroom -->
				<div class="modal fade" id="cont2_livingModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Living Room</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {cont2_living}
				            </div>
				        </div>
				    </div>
				</div>
																<!-- Modal for Cont2 Master Bathroom -->
				<div class="modal fade" id="cont2_covered_porchModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Covered Porch</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {cont2_covered_porch}
				            </div>
				        </div>
				    </div>
				</div>
																				<!-- Modal for Cont2 Master Bathroom -->
				<div class="modal fade" id="cont2_bathroomModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Bathroom</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {cont2_bathroom}
				            </div>
				        </div>
				    </div>
				</div>
																								<!-- Modal for Cont2 Master Bathroom -->
				<div class="modal fade" id="cont2_bed3Modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Bedroom 3</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {cont2_bed3}

				            </div>
				        </div>
				    </div>
				</div>
				"""			


			if(simulation_id == '89'):
				# Map HTML IDs to room IDs duplex 1
				room_id_map = {

					'duplex1_service': 'duplex1_service',
					'duplex1_bathroom': 'duplex1_bathroom',
					'duplex1_bedroom1': 'duplex1_bedroom1',
					'duplex1_bedroom2': 'duplex1_bedroom2',
					'duplex1_kitchen': 'duplex1_kitchen',
					'duplex1_dining': 'duplex1_dining',
					'duplex1_living_room': 'duplex1_living_room',
					'duplex1_porch': 'duplex1_porch'

				}
				result = """
				<img src='assets/blueprints/duplex1.png' usemap="#image-map" style="width:auto; height:auto; margin:auto"> <br>
				<map name="image-map" style="display:none">
				    <area id="duplex1_service" class="droptarget" data-bs-toggle="modal" data-bs-target="#duplex1_serviceModal" alt="service" title="Click to View Service" coords="551,23,743,82" shape="rect">
				    <area id="duplex1_bathroom" class="droptarget" data-bs-toggle="modal" data-bs-target="#duplex1_bathroomModal" alt="bathroom" title="Click to View Bathroom" coords="446,57,538,212" shape="rect">
				    <area id="duplex1_bedroom1" class="droptarget" data-bs-toggle="modal" data-bs-target="#duplex1_bedroom1Modal" alt="bedroom1" title="Click to View Bedroom 1" coords="233,94,428,293" shape="rect">
				    <area id="duplex1_bedroom2" class="droptarget" data-bs-toggle="modal" data-bs-target="#duplex1_bedroom2Modal" alt="bedroom2" title="Click to View Bedroom 2" coords="236,313,427,507" shape="rect">
				    <area id="duplex1_kitchen" class="droptarget" data-bs-toggle="modal" data-bs-target="#duplex1_kitchenModal" alt="kitchen" title="Click to View Kitchen" coords="552,94,748,219" shape="rect">
				    <area id="duplex1_dining" class="droptarget" data-bs-toggle="modal" data-bs-target="#duplex1_diningModal" alt="dining" title="Click to View Dining" coords="447,227,744,398" shape="rect">
				    <area id="duplex1_living_room" class="droptarget" data-bs-toggle="modal" data-bs-target="#duplex1_living_roomModal" alt="living room" title="Click to View Living Room" coords="445,413,738,419,743,606,546,611,536,518,448,506" shape="poly">
				    <area id="duplex1_porch" class="droptarget" data-bs-toggle="modal" data-bs-target="#duplex1_porchModal" alt="porch" title="Click to View Porch" coords="225,529,519,615" shape="rect">
				</map>

				<!-- Modal for Duplex1 Service -->
				<div class="modal fade" id="duplex1_serviceModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Service</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body  d-flex">
				                {duplex1_service}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Duplex1 Bathroom -->
				<div class="modal fade" id="duplex1_bathroomModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Bathroom</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {duplex1_bathroom}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Duplex1 Bedroom1 -->
				<div class="modal fade" id="duplex1_bedroom1Modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Bedroom 1</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {duplex1_bedroom1}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Duplex1 Bedroom2 -->
				<div class="modal fade" id="duplex1_bedroom2Modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Bedroom 2</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {duplex1_bedroom2}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Duplex1 Kitchen -->
				<div class="modal fade" id="duplex1_kitchenModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Kitchen</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {duplex1_kitchen}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Duplex1 Dining -->
				<div class="modal fade" id="duplex1_diningModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Dining Room</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {duplex1_dining}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Duplex1 Living Room -->
				<div class="modal fade" id="duplex1_living_roomModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Living Room</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {duplex1_living_room}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Duplex1 Porch -->
				<div class="modal fade" id="duplex1_porchModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Porch</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {duplex1_porch}
				            </div>
				        </div>
				    </div>
				</div>

				"""

			if(simulation_id == '90'):
				# Map HTML IDs to room IDs Bungalow 1
				room_id_map = {

					'cont3_covered_deck': 'cont3_covered_deck',
					'cont3_laundry': 'cont3_laundry',
					'cont3_greatroom': 'cont3_greatroom',
					'cont3_dining': 'cont3_dining',
					'cont3_wic1': 'cont3_wic1',
					'cont3_wic2': 'cont3_wic2',
					'cont3_wic3': 'cont3_wic3',
					'cont3_master_bathroom': 'cont3_master_bathroom',
					'cont3_master_bedroom': 'cont3_master_bedroom',
					'cont3_foyer': 'cont3_foyer',
					'cont3_bathroom': 'cont3_bathroom',
					'cont3_bedroom': 'cont3_bedroom',
					'cont3_pan': 'cont3_pan',
					'cont3_front_porch': 'cont3_front_porch',
					'cont3_kitchen': 'cont3_kitchen',




				}
				result = """
				<img src='assets/blueprints/contemporary3.png' usemap="#image-map" style="width:auto; height:auto; margin:auto"> <br>
				<map name="image-map" style="display:none">
				    <area id="cont3_covered_deck" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont3_covered_deckModal" alt="service" title="Click to Appliances" coords="84,41,619,177" shape="rect">
				    <area id="cont3_laundry" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont3_laundryModal" alt="bathroom" title="Click to View Appliances" coords="72,217,188,283" shape="rect">
				    <area id="cont3_greatroom" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont3_greatroomModal" alt="bedroom1" title="Click to View Appliances" coords="202,202,393,411" shape="rect">
				    <area id="cont3_dining" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont3_diningModal" alt="bedroom2" title="Click to View Appliances" coords="410,214,508,414" shape="rect">
				    <area id="cont3_wic1" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont3_wic1Modal" alt="kitchen" title="Click to View Appliances" coords="71,304,187,357" shape="rect">
				    <area id="cont3_wic2" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont3_wic2Modal" alt="dining" title="Click to View Appliances" coords="202,420,273,465" shape="rect">
				    <area id="cont3_wic3" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont3_wic3Modal" alt="living room" title="Click to View Appliances" coords="514,420,570,476" shape="rect">
				    <area id="cont3_master_bathroom" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont3_master_bathroomModal" alt="porch" title="Click to View Appliances" coords="77,369,184,463" shape="rect">
					<area id="cont3_master_bedroom" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont3_master_bedroomModal" alt="porch" title="Click to View Appliances" coords="74,481,272,623" shape="rect">
				    <area id="cont3_foyer" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont3_foyerModal" alt="porch" title="Click to View Appliances" coords="290,419,427,624" shape="rect">
					<area id="cont3_bathroom" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont3_bathroomModal" alt="porch" title="Click to View Appliances" coords="437,421,501,536" shape="rect">
				    <area id="cont3_bedroom" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont3_bedroomModal" alt="porch" title="Click to View Appliances" coords="514,493,640,489,637,623,518,622,445,623,440,580,440,546,516,549" shape="poly">
				    <area id="cont3_front_porch" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont3_front_porchModal" alt="porch" title="Click to View Appliances" coords="233,643,480,816" shape="rect">
				     <area id="cont3_kitchen" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont3_kitchenModal" alt="porch" title="Click to View Appliances" coords="518,212,644,411" shape="rect">
				       <area id="cont3_pan" class="droptarget" data-bs-toggle="modal" data-bs-target="#cont3_panModal" alt="porch" title="Click to View Appliances" coords="580,422,637,477" shape="rect">

				</map>


									<!-- Modal for Duplex1 Covered Deck -->
					<div class="modal fade" id="cont3_front_porchModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
					    <div class="modal-dialog modal-dialog-centered" role="document">
					        <div class="modal-content">
					            <div class="modal-header">
					                <h5 class="modal-title" id="exampleModalLabel">Front Porch</h5>
					                <div style="width:100px" class="row">
					                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
					                    <div class="col p-2">
					                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					                    </div>
					                </div>
					            </div>
					            <div class="modal-body d-flex">
					                {cont3_front_porch}
					            </div>
					        </div>
					    </div>
					</div>

										<!-- Modal for Duplex1 Covered Deck -->
					<div class="modal fade" id="cont3_kitchenModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
					    <div class="modal-dialog modal-dialog-centered" role="document">
					        <div class="modal-content">
					            <div class="modal-header">
					                <h5 class="modal-title" id="exampleModalLabel">Kitchen</h5>
					                <div style="width:100px" class="row">
					                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
					                    <div class="col p-2">
					                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					                    </div>
					                </div>
					            </div>
					            <div class="modal-body d-flex">
					                {cont3_kitchen}
					            </div>
					        </div>
					    </div>
					</div>

					<!-- Modal for Duplex1 Covered Deck -->
					<div class="modal fade" id="cont3_covered_deckModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
					    <div class="modal-dialog modal-dialog-centered" role="document">
					        <div class="modal-content">
					            <div class="modal-header">
					                <h5 class="modal-title" id="exampleModalLabel">Covered Deck</h5>
					                <div style="width:100px" class="row">
					                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
					                    <div class="col p-2">
					                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					                    </div>
					                </div>
					            </div>
					            <div class="modal-body d-flex">
					                {cont3_covered_deck}
					            </div>
					        </div>
					    </div>
					</div>

					<!-- Modal for Duplex1 Laundry -->
					<div class="modal fade" id="cont3_laundryModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
					    <div class="modal-dialog modal-dialog-centered" role="document">
					        <div class="modal-content">
					            <div class="modal-header">
					                <h5 class="modal-title" id="exampleModalLabel">Laundry</h5>
					                <div style="width:100px" class="row">
					                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
					                    <div class="col p-2">
					                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					                    </div>
					                </div>
					            </div>
					            <div class="modal-body d-flex">
					                {cont3_laundry}
					            </div>
					        </div>
					    </div>
					</div>

					<!-- Modal for Duplex1 Great Room -->
					<div class="modal fade" id="cont3_greatroomModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
					    <div class="modal-dialog modal-dialog-centered" role="document">
					        <div class="modal-content">
					            <div class="modal-header">
					                <h5 class="modal-title" id="exampleModalLabel">Great Room</h5>
					                <div style="width:100px" class="row">
					                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
					                    <div class="col p-2">
					                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					                    </div>
					                </div>
					            </div>
					            <div class="modal-body d-flex">
					                {cont3_greatroom}
					            </div>
					        </div>
					    </div>
					</div>

					<!-- Modal for Duplex1 Dining -->
					<div class="modal fade" id="cont3_diningModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
					    <div class="modal-dialog modal-dialog-centered" role="document">
					        <div class="modal-content">
					            <div class="modal-header">
					                <h5 class="modal-title" id="exampleModalLabel">Dining</h5>
					                <div style="width:100px" class="row">
					                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
					                    <div class="col p-2">
					                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					                    </div>
					                </div>
					            </div>
					            <div class="modal-body d-flex">
					                {cont3_dining}
					            </div>
					        </div>
					    </div>
					</div>

					<!-- Modal for Duplex1 Walk-In Closet 1 -->
					<div class="modal fade" id="cont3_wic1Modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
					    <div class="modal-dialog modal-dialog-centered" role="document">
					        <div class="modal-content">
					            <div class="modal-header">
					                <h5 class="modal-title" id="exampleModalLabel">Walk-In Closet 1</h5>
					                <div style="width:100px" class="row">
					                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
					                    <div class="col p-2">
					                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					                    </div>
					                </div>
					            </div>
					            <div class="modal-body d-flex">
					                {cont3_wic1}
					            </div>
					        </div>
					    </div>
					</div>

					<!-- Modal for Duplex1 Walk-In Closet 2 -->
					<div class="modal fade" id="cont3_wic2Modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
					    <div class="modal-dialog modal-dialog-centered" role="document">
					        <div class="modal-content">
					            <div class="modal-header">
					                <h5 class="modal-title" id="exampleModalLabel">Walk-In Closet 2</h5>
					                <div style="width:100px" class="row">
					                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
					                    <div class="col p-2">
					                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					                    </div>
					                </div>
					            </div>
					            <div class="modal-body d-flex">
					                {cont3_wic2}
					            </div>
					        </div>
					    </div>
					</div>

					<!-- Modal for Duplex1 Walk-In Closet 3 -->
					<div class="modal fade" id="cont3_wic3Modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
					    <div class="modal-dialog modal-dialog-centered" role="document">
					        <div class="modal-content">
					            <div class="modal-header">
					                <h5 class="modal-title" id="exampleModalLabel">Walk-In Closet 3</h5>
					                <div style="width:100px" class="row">
					                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
					                    <div class="col p-2">
					                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					                    </div>
					                </div>
					            </div>
					            <div class="modal-body d-flex">
					                {cont3_wic3}
					            </div>
					        </div>
					    </div>
					</div>

					<!-- Modal for Duplex1 Master Bathroom -->
					<div class="modal fade" id="cont3_master_bathroomModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
					    <div class="modal-dialog modal-dialog-centered" role="document">
					        <div class="modal-content">
					            <div class="modal-header">
					                <h5 class="modal-title" id="exampleModalLabel">Master Bathroom</h5>
					                <div style="width:100px" class="row">
					                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
					                    <div class="col p-2">
					                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					                    </div>
					                </div>
					            </div>
					            <div class="modal-body d-flex">
					                {cont3_master_bathroom}
					            </div>
					        </div>
					    </div>
					</div>

					<!-- Modal for Duplex1 Master Bedroom -->
					<div class="modal fade" id="cont3_master_bedroomModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
					    <div class="modal-dialog modal-dialog-centered" role="document">
					        <div class="modal-content">
					            <div class="modal-header">
					                <h5 class="modal-title" id="exampleModalLabel">Master Bedroom</h5>
					                <div style="width:100px" class="row">
					                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
					                    <div class="col p-2">
					                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					                    </div>
					                </div>
					            </div>
					            <div class="modal-body d-flex">
					                {cont3_master_bedroom}
					            </div>
					        </div>
					    </div>
					</div>

					<!-- Modal for Duplex1 Foyer -->
					<div class="modal fade" id="cont3_foyerModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
					    <div class="modal-dialog modal-dialog-centered" role="document">
					        <div class="modal-content">
					            <div class="modal-header">
					                <h5 class="modal-title" id="exampleModalLabel">Foyer</h5>
					                <div style="width:100px" class="row">
					                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
					                    <div class="col p-2">
					                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					                    </div>
					                </div>
					            </div>
					            <div class="modal-body d-flex">
					                {cont3_foyer}
					            </div>
					        </div>
					    </div>
					</div>

					<!-- Modal for Duplex1 Foyer -->
					<div class="modal fade" id="cont3_bathroomModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
					    <div class="modal-dialog modal-dialog-centered" role="document">
					        <div class="modal-content">
					            <div class="modal-header">
					                <h5 class="modal-title" id="exampleModalLabel">Bathroom</h5>
					                <div style="width:100px" class="row">
					                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
					                    <div class="col p-2">
					                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					                    </div>
					                </div>
					            </div>
					            <div class="modal-body d-flex">
					                {cont3_bathroom}
					            </div>
					        </div>
					    </div>
					</div>

										<!-- Modal for Duplex1 Foyer -->
					<div class="modal fade" id="cont3_bedroomModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
					    <div class="modal-dialog modal-dialog-centered" role="document">
					        <div class="modal-content">
					            <div class="modal-header">
					                <h5 class="modal-title" id="exampleModalLabel">Bedroom 2</h5>
					                <div style="width:100px" class="row">
					                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
					                    <div class="col p-2">
					                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					                    </div>
					                </div>
					            </div>
					            <div class="modal-body d-flex">
					                {cont3_bedroom}
					            </div>
					        </div>
					    </div>
					</div>
															<!-- Modal for Duplex1 Foyer -->
					<div class="modal fade" id="cont3_panModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
					    <div class="modal-dialog modal-dialog-centered" role="document">
					        <div class="modal-content">
					            <div class="modal-header">
					                <h5 class="modal-title" id="exampleModalLabel">Pan</h5>
					                <div style="width:100px" class="row">
					                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
					                    <div class="col p-2">
					                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					                    </div>
					                </div>
					            </div>
					            <div class="modal-body d-flex">
					                {cont3_pan}
					            </div>
					        </div>
					    </div>
					</div>
				"""




			if(simulation_id == '91'):
				# Map HTML IDs to room IDs Bungalow 2
				room_id_map = {

					'bungalow2_open_terrace': 'bungalow2_open_terrace',
					'bungalow2_kitchen': 'bungalow2_kitchen',
					'bungalow2_dining': 'bungalow2_dining',
					'bungalow2_bedroom1': 'bungalow2_bedroom1',
					'bungalow2_bedroom2': 'bungalow2_bedroom2',
					'bungalow2_t_b': 'bungalow2_t_b',
					'bungalow2_wic': 'bungalow2_wic',
					'bungalow2_garage': 'bungalow2_garage',
					'bungalow2_master_bedroom': 'bungalow2_master_bedroom',
					'bungalow2_living_room': 'bungalow2_living_room',
					'bungalow2_bathroom': 'bungalow2_bathroom',
					'bungalow2_porch': 'bungalow2_porch'

				}
				result = """
				
				<map name="image-map" style="display:none">
				    <area id="bungalow2_open_terrace" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow2_open_terraceModal" alt="dining-kitchen1" title="Click to View Appliances" coords="437,98,630,157" shape="rect">
				    <area id="bungalow2_kitchen" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow2_kitchenModal" alt="dining-kitchen1" title="Click to View Appliances" coords="268,126,415,246" shape="rect">
				    <area id="bungalow2_dining" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow2_diningModal" alt="dining-kitchen1" title="Click to View Appliances" coords="438,172,627,343" shape="rect">
				    <area id="bungalow2_bedroom1" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow2_bedroom1Modal" alt="dining-kitchen1" title="Click to View Appliances" coords="643,165,783,335" shape="rect">
				    <area id="bungalow2_bedroom2" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow2_bedroom2Modal" alt="dining-kitchen1" title="Click to View Appliances" coords="642,439,782,609" shape="rect">
				    <area id="bungalow2_t_b" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow2_t_bModal" alt="dining-kitchen1" title="Click to View Appliances" coords="257,274,357,334" shape="rect">
				    <area id="bungalow2_wic" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow2_wicModal" alt="dining-kitchen1" title="Click to View Appliances" coords="367,266,422,345" shape="rect">
				    <area id="bungalow2_garage" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow2_garageModal" alt="dining-kitchen1" title="Click to View Appliances" coords="40,354,235,543" shape="rect">
				    <area id="bungalow2_master_bedroom" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow2_master_bedroomModal" alt="dining-kitchen1" title="Click to View Appliances" coords="262,385,418,545" shape="rect">
				    <area id="bungalow2_living_room" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow2_living_roomModal" alt="dining-kitchen1" title="Click to View Appliances" coords="437,367,625,545" shape="rect">
					<area id="bungalow2_bathroom" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow2_bathroomModal" alt="dining-kitchen1" title="Click to View Appliances" coords="700,351,807,421" shape="rect">
					<area id="bungalow2_porch" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow2_porchModal" alt="dining-kitchen1" title="Click to View Appliances" coords="545,532,374,487" shape="rect">

				</map>

				<img src='assets/blueprints/bungalow2.png' usemap="#image-map" style="width:auto; height:auto"><br>

					<!-- Bootstrap Modal for Bungalow2 Open Terrace -->
					<div class="modal fade" id="bungalow2_open_terraceModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
					    <div class="modal-dialog modal-dialog-centered" role="document">
					        <div class="modal-content">
					            <div class="modal-header">
					                <h5 class="modal-title" id="exampleModalLabel">Open Terrace</h5>
					                <div style="width:100px" class="row">
					                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
					                    <div class="col p-2">
					                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					                    </div>
					                </div>
					            </div>
					            <div class="modal-body d-flex">
					                {bungalow2_open_terrace}
					            </div>
					        </div>
					    </div>
					</div>

					<!-- Bootstrap Modal for Bungalow2 Kitchen -->
					<div class="modal fade" id="bungalow2_kitchenModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
					    <div class="modal-dialog modal-dialog-centered" role="document">
					        <div class="modal-content">
					            <div class="modal-header">
					                <h5 class="modal-title" id="exampleModalLabel">Kitchen</h5>
					                <div style="width:100px" class="row">
					                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
					                    <div class="col p-2">
					                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					                    </div>
					                </div>
					            </div>
					            <div class="modal-body d-flex">
					                {bungalow2_kitchen}
					            </div>
					        </div>
					    </div>
					</div>

					<!-- Bootstrap Modal for Bungalow2 Dining -->
					<div class="modal fade" id="bungalow2_diningModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
					    <div class="modal-dialog modal-dialog-centered" role="document">
					        <div class="modal-content">
					            <div class="modal-header">
					                <h5 class="modal-title" id="exampleModalLabel">Dining</h5>
					                <div style="width:100px" class="row">
					                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
					                    <div class="col p-2">
					                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					                    </div>
					                </div>
					            </div>
					            <div class="modal-body d-flex">
					                {bungalow2_dining}
					            </div>
					        </div>
					    </div>
					</div>

					<!-- Bootstrap Modal for Bungalow2 Bedroom 1 -->
					<div class="modal fade" id="bungalow2_bedroom1Modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
					    <div class="modal-dialog modal-dialog-centered" role="document">
					        <div class="modal-content">
					            <div class="modal-header">
					                <h5 class="modal-title" id="exampleModalLabel">Bedroom 1</h5>
					                <div style="width:100px" class="row">
					                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
					                    <div class="col p-2">
					                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					                    </div>
					                </div>
					            </div>
					            <div class="modal-body d-flex">
					                {bungalow2_bedroom1}
					            </div>
					        </div>
					    </div>
					</div>

					<!-- Bootstrap Modal for Bungalow2 Bedroom 2 -->
					<div class="modal fade" id="bungalow2_bedroom2Modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
					    <div class="modal-dialog modal-dialog-centered" role="document">
					        <div class="modal-content">
					            <div class="modal-header">
					                <h5 class="modal-title" id="exampleModalLabel">Bedroom 2</h5>
					                <div style="width:100px" class="row">
					                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
					                    <div class="col p-2">
					                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					                    </div>
					                </div>
					            </div>
					            <div class="modal-body d-flex">
					                {bungalow2_bedroom2}
					            </div>
					        </div>
					    </div>
					</div>

					<!-- Bootstrap Modal for Bungalow2 T-B -->
					<div class="modal fade" id="bungalow2_t_bModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
					    <div class="modal-dialog modal-dialog-centered" role="document">
					        <div class="modal-content">
					            <div class="modal-header">
					                <h5 class="modal-title" id="exampleModalLabel">T-B</h5>
					                <div style="width:100px" class="row">
					                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
					                    <div class="col p-2">
					                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					                    </div>
					                </div>
					            </div>
					            <div class="modal-body d-flex">
					                {bungalow2_t_b}
					            </div>
					        </div>
					    </div>
					</div>

					<!-- Bootstrap Modal for Bungalow2 WIC -->
					<div class="modal fade" id="bungalow2_wicModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
					    <div class="modal-dialog modal-dialog-centered" role="document">
					        <div class="modal-content">
					            <div class="modal-header">
					                <h5 class="modal-title" id="exampleModalLabel">WIC</h5>
					                <div style="width:100px" class="row">
					                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
					                    <div class="col p-2">
					                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					                    </div>
					                </div>
					            </div>
					            <div class="modal-body d-flex">
					                {bungalow2_wic}
					            </div>
					        </div>
					    </div>
					</div>

					<!-- Bootstrap Modal for Bungalow2 Garage -->
					<div class="modal fade" id="bungalow2_garageModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
					    <div class="modal-dialog modal-dialog-centered" role="document">
					        <div class="modal-content">
					            <div class="modal-header">
					                <h5 class="modal-title" id="exampleModalLabel">Garage</h5>
					                <div style="width:100px" class="row">
					                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
					                    <div class="col p-2">
					                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					                    </div>
					                </div>
					            </div>
					            <div class="modal-body d-flex">
					                {bungalow2_garage}
					            </div>
					        </div>
					    </div>
					</div>

					<!-- Bootstrap Modal for Bungalow2 Master Bedroom -->
					<div class="modal fade" id="bungalow2_master_bedroomModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
					    <div class="modal-dialog modal-dialog-centered" role="document">
					        <div class="modal-content">
					            <div class="modal-header">
					                <h5 class="modal-title" id="exampleModalLabel">Master Bedroom</h5>
					                <div style="width:100px" class="row">
					                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
					                    <div class="col p-2">
					                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					                    </div>
					                </div>
					            </div>
					            <div class="modal-body d-flex">
					                {bungalow2_master_bedroom}
					            </div>
					        </div>
					    </div>
					</div>

					<!-- Bootstrap Modal for Bungalow2 Living Room -->
					<div class="modal fade" id="bungalow2_living_roomModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
					    <div class="modal-dialog modal-dialog-centered" role="document">
					        <div class="modal-content">
					            <div class="modal-header">
					                <h5 class="modal-title" id="exampleModalLabel">Living Room</h5>
					                <div style="width:100px" class="row">
					                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
					                    <div class="col p-2">
					                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					                    </div>
					                </div>
					            </div>
					            <div class="modal-body d-flex">
					                {bungalow2_living_room}
					            </div>
					        </div>
					    </div>
					</div>

					<!-- Bootstrap Modal for Bungalow2 Bathroom -->
					<div class="modal fade" id="bungalow2_bathroomModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
					    <div class="modal-dialog modal-dialog-centered" role="document">
					        <div class="modal-content">
					            <div class="modal-header">
					                <h5 class="modal-title" id="exampleModalLabel">Bathroom</h5>
					                <div style="width:100px" class="row">
					                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
					                    <div class="col p-2">
					                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					                    </div>
					                </div>
					            </div>
					            <div class="modal-body d-flex">
					                {bungalow2_bathroom}
					            </div>
					        </div>
					    </div>
					</div>

					<!-- Bootstrap Modal for Bungalow2 Porch -->
					<div class="modal fade" id="bungalow2_porchModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
					    <div class="modal-dialog modal-dialog-centered" role="document">
					        <div class="modal-content">
					            <div class="modal-header">
					                <h5 class="modal-title" id="exampleModalLabel">Porch</h5>
					                <div style="width:100px" class="row">
					                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
					                    <div class="col p-2">
					                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
					                    </div>
					                </div>
					            </div>
					            <div class="modal-body d-flex">
					                {bungalow2_porch}
					            </div>
					        </div>
					    </div>
					</div>

				"""

			if(simulation_id == '92'):
				# Map HTML IDs to room IDs Bungalow 1
				room_id_map = {

					'bungalow3_bedroom1': 'bungalow3_bedroom1',
					'bungalow3_bedroom2': 'bungalow3_bedroom2',
					'bungalow3_kitchen': 'bungalow3_kitchen',
					'bungalow3_dining': 'bungalow3_dining',
					'bungalow3_laundry': 'bungalow3_laundry',
					'bungalow3_bathroom': 'bungalow3_bathroom',
					'bungalow3_living_room': 'bungalow3_living_room',
					'bungalow3_porch': 'bungalow3_porch'

				}
				result = """
				<img src='assets/blueprints/bungalow3.png' usemap="#image-map" style="width:auto; height:auto"><br>
				<map name="image-map" style="display:none">
				    <area id="bungalow3_bedroom1" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow3_bedroom1Modal" alt="dining-kitchen1" title="Click to View Appliances" coords="164,109,413,360" shape="rect">
				    <area id="bungalow3_bedroom2" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow3_bedroom2Modal" alt="dining-kitchen1" title="Click to View Appliances" coords="158,540,423,795" shape="rect">
				    <area id="bungalow3_kitchen" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow3_kitchenModal" alt="dining-kitchen1" title="Click to View Appliances" coords="457,97,720,326" shape="rect">
				    <area id="bungalow3_dining" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow3_diningModal" alt="dining-kitchen1" title="Click to View Appliances" coords="452,336,722,508" shape="rect">
				    <area id="bungalow3_laundry" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow3_laundryModal" alt="dining-kitchen1" title="Click to View Appliances" coords="677,520,567,397" shape="rect">
				    <area id="bungalow3_bathroom" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow3_bathroomModal" alt="dining-kitchen1" title="Click to View Appliances" coords="91,390,331,504" shape="rect">
				    <area id="bungalow3_living_room" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow3_living_roomModal" alt="dining-kitchen1" title="Click to View Appliances" coords="455,514,723,791" shape="rect">
				    <area id="bungalow3_porch" class="droptarget" data-bs-toggle="modal" data-bs-target="#bungalow3_porchModal" alt="dining-kitchen1" title="Click to View Appliances" coords="434,831,747,950" shape="rect">
				</map>

				<!-- Modal for Bungalow3 Bedroom1 -->
				<div class="modal fade" id="bungalow3_bedroom1Modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Bedroom 1</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {bungalow3_bedroom1}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Bungalow3 Bedroom2 -->
				<div class="modal fade" id="bungalow3_bedroom2Modal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Bedroom 2</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {bungalow3_bedroom2}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Bungalow3 Kitchen -->
				<div class="modal fade" id="bungalow3_kitchenModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Kitchen</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {bungalow3_kitchen}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Bungalow3 Dining -->
				<div class="modal fade" id="bungalow3_diningModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Dining Room</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {bungalow3_dining}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Bungalow3 Laundry -->
				<div class="modal fade" id="bungalow3_laundryModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Laundry</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {bungalow3_laundry}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Bungalow3 Bathroom -->
				<div class="modal fade" id="bungalow3_bathroomModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Bathroom</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {bungalow3_bathroom}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Bungalow3 Living Room -->
				<div class="modal fade" id="bungalow3_living_roomModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Living Room</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {bungalow3_living_room}
				            </div>
				        </div>
				    </div>
				</div>

				<!-- Modal for Bungalow3 Porch -->
				<div class="modal fade" id="bungalow3_porchModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
				    <div class="modal-dialog modal-dialog-centered" role="document">
				        <div class="modal-content">
				            <div class="modal-header">
				                <h5 class="modal-title" id="exampleModalLabel">Porch</h5>
				                <div style="width:100px" class="row">
				                    <img src="delete.png" style="margin: auto; width: 35px!important;" class="droptarget" id="delete" style="width:45px;height:45px;border:none!important;">
				                    <div class="col p-2">
				                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
				                    </div>
				                </div>
				            </div>
				            <div class="modal-body d-flex">
				                {bungalow3_porch}
				            </div>
				        </div>
				    </div>
				</div>

				"""

			# Fill in the placeholders with images
			for html_id, room_id in room_id_map.items():
			    images_html = ""
			    if room_id in grouped_data:
			        images_html = "".join(
						f'''
						    <span style="width:90px!important; padding:5px" data-bs-toggle="modal" data-bs-target="#appModal" data-input-hr="{canvas_id}_{watt}_{applianceName}_{grouped_data[room_id]['roomName']}">
						        <input type="hidden" id="{canvas_id}_{watt}_{applianceName}_{grouped_data[room_id]['roomName']}" class="toggleInput" value="1">
						        
						        <div>
						            <img data-bs-toggle="tooltip" data-bs-placement="top" title="{applianceName} - {watt} W " draggable="true" data-is-update="1" data-canvas-id="{canvas_id}" 
						            data-custom-id="{room_id}" id="{image_id}" src="assets/uploads/{image}" style="height:30px;" />
						            
						            <span id="{canvas_id}_{watt}_{applianceName}_{grouped_data[room_id]['roomName']}_isOn" style="width: 10px; height: 10px; background: green;border: .5px solid white; border-radius: 50%; margin-left: 7px; margin-right: 7px; display: inline-block;"></span>
						        </div>
						    </span>
						'''

			            for image, image_id, canvas_id, watt, applianceName in grouped_data[room_id]['images']
			        )
			    result = result.replace(f'{{{html_id}}}', images_html)

			# Replace any remaining placeholders with empty strings
			for html_id in room_id_map.keys():
				result = result.replace(f'{{{html_id}}}', '')

			return {'message': result}
		except sqlite3.Error as e:
			print(f"An error occurred: {e}")
		finally:
			if connection:
				connection.close()


	# def fetch_room(self, simulation_id):
	#     try:
	#         # Connect to the SQLite database
	#         connection = sqlite3.connect('ecoenergy.db')
	#         cursor = connection.cursor()
			
	#         # Query to fetch room and canvas details
	#         query = """SELECT room.id AS roomId, room.name AS roomName, sub_appliance.image AS applianceImage, 
	#         sub_appliance.id AS applianceImageId, simulation.*, canvas.id AS canvasRow
	#         FROM canvas 
	#         INNER JOIN room ON room.id = canvas.room_id
	#         INNER JOIN sub_appliance ON sub_appliance.id = canvas.appliance_id
	#         INNER JOIN simulation ON simulation.id = canvas.simulation_id 
	#         WHERE canvas.simulation_id = ?;"""
	#         cursor.execute(query, (simulation_id,))
	#         rows = cursor.fetchall()  # Fetch all rows from the query result

	#         columns = [description[0] for description in cursor.description]  # Get column names

	#         # Fetch all rooms
	#         query_rooms = """SELECT room.id AS roomId, room.name AS roomName FROM room
	#                          WHERE room.simulation_id = ?;"""
	#         cursor.execute(query_rooms, (simulation_id,))
	#         rooms = cursor.fetchall()

	#         # Group images by roomId
	#         grouped_data = {}
	#         for row in rows:
	#             row_data = {columns[i]: row[i] for i in range(len(row))}
	#             room_id = row_data['roomId']
	#             canvas_id = row_data['canvasRow']  # Fetch the canvas.id
				
	#             if room_id not in grouped_data:
	#                 grouped_data[room_id] = {
	#                     'roomName': row_data['roomName'],
	#                     'canvasRow': canvas_id,
	#                     'images': []
	#                 }
	#             # Append image, image_id, and canvas_id to the list of images
	#             grouped_data[room_id]['images'].append((row_data['applianceImage'], row_data['applianceImageId'], canvas_id))

	#         # Generate HTML
	#         result = ""
	#         for room in rooms:
	#             room_id = room[0]
	#             room_name = room[1]
	#             images_html = ""
	#             if room_id in grouped_data:
	#                 images_html = "".join(
	#                     f'<img draggable="true" data-is-update="1" data-canvas-id="{canvas_id}" data-custom-id="{room_id}" id="{image_id}" src="assets/uploads/{image}" style="width:60px; height:60px;" />' 
	#                     for image, image_id, canvas_id in grouped_data[room_id]['images']
	#                 )
	#             result += f"""<div class="col-3">
	#                             {room_name}
	#                             <div class="droptarget" id="{room_id}">
	#                                 {images_html}
	#                             </div>
	#                         </div>"""

	#         return {'message': result}
		
	#     except sqlite3.Error as e:
	#         return {'error': f"Error: {e}"}
	#     finally:
	#         cursor.close()
	#         connection.close()


	def get_suggestions(self, target_bill, target_hours, rate_per_hr, simulation_id):
	    try:
	        # Connect to the SQLite database
	        connection = sqlite3.connect('ecoenergy.db')
	        cursor = connection.cursor()

	        # Calculate target watt-hours based on the bill
	        rate_per_kwh =  float(rate_per_hr)  # PESO per kilowatt-hour
	        target_wh = (float(target_bill) / rate_per_kwh) * 1000  # Convert bill to watt-hours

	        # Query to get appliance data filtered by simulation_id
	        query = '''
	            SELECT canvas.id, canvas.room_id, canvas.appliance_id, sub_appliance.watt, sub_appliance.name 
	            FROM canvas
	            JOIN sub_appliance ON canvas.appliance_id = sub_appliance.id
	            WHERE canvas.simulation_id = ?
	        '''
	        cursor.execute(query, (simulation_id,))
	        rows = cursor.fetchall()
	        
	        # Start building the HTML output for the scrollable column
	        html_output = '''
	            <div class="container">
	                <div class="row">
	        '''

	        current_room_id = None
	        total_wh_consumption = 0
	        room_wh_consumption = 0
	        room_bill = 0

	        room_data = {}

	        # Calculate the total watts for all appliances
	        total_wattage = sum(float(row[3]) for row in rows if row[3])

	        for row in rows:
	            room_id, appliance_id, watt, appliance_name = row[1], row[2], row[3], row[4]
	            watt = float(watt) if watt else 0

	            # Calculate suggested hours based on the total wattage
	            if total_wattage > 0:
	                suggested_hours = (target_wh / total_wattage)
	            else:
	                suggested_hours = 0

	            # Calculate watt-hours and bill for the appliance
	            appliance_wh = watt * suggested_hours
	            appliance_bill = (appliance_wh / 1000) * rate_per_kwh

	            # Accumulate total consumption and bill
	            total_wh_consumption += appliance_wh

	            if room_id not in room_data:
	                room_query = 'SELECT name FROM room WHERE id = ?'
	                cursor.execute(room_query, (room_id,))
	                room_name = cursor.fetchone()
	                room_name = room_name[0] if room_name else "Unknown Room"
	                room_data[room_id] = {
	                    'room_name': room_name,
	                    'appliances': [],
	                    'room_wh_consumption': 0,
	                    'room_bill': 0
	                }

	            room_data[room_id]['appliances'].append({
	                'appliance_name': appliance_name,
	                'suggested_hours': suggested_hours,
	                'appliance_bill': appliance_bill
	            })
	            room_data[room_id]['room_wh_consumption'] += appliance_wh
	            room_data[room_id]['room_bill'] += appliance_bill

	        for room_id, room in room_data.items():
	            html_output += f'''
	                <div class="col-md-12 border room-section mb-3" style="height:auto">
	                    <p class="text-primary">{room['room_name']}</p>
	                    <div class="appliance-list" style="height:auto">
	            '''
	            for appliance in room['appliances']:
	                html_output += f'''
	                    <div class="appliance" style="height:auto">
	                        <span>Appliance: {appliance['appliance_name']}</span><br>
	                        <span>Suggested Usage: {appliance['suggested_hours']:.2f} hours</span><br>
	                        <span>Appliance Bill: {appliance['appliance_bill']:.2f} PESO</span>
	                        <hr style="width:auto">
	                    </div>
	                '''
	            html_output += f'''
	                    </div>
	                    <div class="room-total-bill">
	                        <p>Total Room Bill: {room['room_bill']:.2f} PESO</p>
	                    </div>
	                </div>
	            '''

	        # Calculate the total bill based on the total watt-hours consumed
	        total_bill = (total_wh_consumption / 1000) * rate_per_kwh

	        # Append the total bill to the HTML output
	        html_output += f'''
	            <div class="col-12 total-bill">
	                <p>Total Estimated Bill: {total_bill:.2f} PESO</p>
	            </div>
	        '''

	        # Close the main row and container divs
	        html_output += '</div></div>'

	        return {'message': html_output}

	    except Exception as e:
	        print(f"Error occurred: {e}")
	        return {'message': '<p>An error occurred while fetching suggestions.</p>'}

	    finally:
	        cursor.close()
	        connection.close()



	def get_suggestions_energy(self, target_kwh, rate_per_hr, simulation_id):
	    try:
	        # Connect to the SQLite database
	        connection = sqlite3.connect('ecoenergy.db')
	        cursor = connection.cursor()

	        # Calculate target watt-hours based on the kWh input
	        target_wh = float(target_kwh) * 1000  # Convert kWh to watt-hours

	        # Query to get appliance data filtered by simulation_id
	        query = '''
	            SELECT canvas.id, canvas.room_id, canvas.appliance_id, sub_appliance.watt, sub_appliance.name 
	            FROM canvas
	            JOIN sub_appliance ON canvas.appliance_id = sub_appliance.id
	            WHERE canvas.simulation_id = ?
	        '''
	        cursor.execute(query, (simulation_id,))
	        rows = cursor.fetchall()
	        
	        # Start building the HTML output for the scrollable column
	        html_output = '''
	            <div class="container">
	                <div class="row">
	        '''

	        current_room_id = None
	        total_wh_consumption = 0
	        room_wh_consumption = 0
	        room_bill = 0

	        room_data = {}

	        # Calculate the total watts for all appliances
	        total_wattage = sum(float(row[3]) for row in rows if row[3])

	        for row in rows:
	            room_id, appliance_id, watt, appliance_name = row[1], row[2], row[3], row[4]
	            watt = float(watt) if watt else 0

	            # Calculate suggested hours based on the total wattage
	            if total_wattage > 0:
	                suggested_hours = (target_wh / total_wattage)
	            else:
	                suggested_hours = 0

	            # Calculate watt-hours and bill for the appliance
	            appliance_wh = watt * suggested_hours
	            rate_per_kwh =  float(rate_per_hr)  # PESO per kilowatt-hour
	            appliance_bill = (appliance_wh / 1000) * rate_per_kwh

	            # Accumulate total consumption and bill
	            total_wh_consumption += appliance_wh

	            if room_id not in room_data:
	                room_query = 'SELECT name FROM room WHERE id = ?'
	                cursor.execute(room_query, (room_id,))
	                room_name = cursor.fetchone()
	                room_name = room_name[0] if room_name else "Unknown Room"
	                room_data[room_id] = {
	                    'room_name': room_name,
	                    'appliances': [],
	                    'room_wh_consumption': 0,
	                    'room_bill': 0
	                }

	            room_data[room_id]['appliances'].append({
	                'appliance_name': appliance_name,
	                'suggested_hours': suggested_hours,
	                'appliance_bill': appliance_bill
	            })
	            room_data[room_id]['room_wh_consumption'] += appliance_wh
	            room_data[room_id]['room_bill'] += appliance_bill

	        for room_id, room in room_data.items():
	            html_output += f'''
	                <div class="col-md-12 border room-section mb-3" style="height:auto">
	                    <p class="text-primary">{room['room_name']}</p>
	                    <div class="appliance-list" style="height:auto">
	            '''
	            for appliance in room['appliances']:
	                html_output += f'''
	                    <div class="appliance" style="height:auto">
	                        <span>Appliance: {appliance['appliance_name']}</span><br>
	                        <span>Suggested Usage: {appliance['suggested_hours']:.2f} hours</span><br>
	                        <span>Appliance Bill: {appliance['appliance_bill']:.2f} PESO</span>
	                        <hr style="width:auto">
	                    </div>
	                '''
	            html_output += f'''
	                    </div>
	                    <div class="room-total-bill">
	                        <p>Total Room Bill: {room['room_bill']:.2f} PESO</p>
	                    </div>
	                </div>
	            '''

	        # Calculate the total bill based on the total watt-hours consumed
	        total_bill = (total_wh_consumption / 1000) * rate_per_kwh

	        # Append the total bill to the HTML output
	        html_output += f'''
	            <div class="col-12 total-bill">
	                <p>Total Estimated Bill: {total_bill:.2f} PESO</p>
	            </div>
	        '''

	        # Close the main row and container divs
	        html_output += '</div></div>'

	        return {'message': html_output}

	    except Exception as e:
	        print(f"Error occurred: {e}")
	        return {'message': '<p>An error occurred while fetching suggestions.</p>'}

	    finally:
	        cursor.close()
	        connection.close()






	
	def fetch_data(self):
		try:
			# Connect to the SQLite database (it will create the file if it doesn't exist)
			connection = sqlite3.connect('ecoenergy.db')
			cursor = connection.cursor()
			
			# Execute the query
			cursor.execute("SELECT * FROM users;")
			rows = cursor.fetchall()  # Fetch all rows from the query result
			columns = [description[0] for description in cursor.description]  # Get column names

			# Return the fetched data as a string (for simplicity)
			result = ""
			for row in rows:
				row_data = {columns[i]: row[i] for i in range(len(row))}  # Create dict of column names and row values
				result += f"""<tr>
								<td>{row_data['id']}</td>
								<td>{row_data['firstname']}</td>
								<td>{row_data['lastname']}</td>
							</tr>"""
	  
			return {'message': result}
		
		except sqlite3.Error as e:
			return {'message': f"Error: {e}"}
		finally:
			cursor.close()
			connection.close()

	def search_data(self, searchByName):
		try:
			# Connect to the SQLite database
			connection = sqlite3.connect('ecoenergy.db')
			cursor = connection.cursor()

			# Query to search name
			query = "SELECT * FROM users WHERE firstname LIKE ? OR lastname LIKE ?;"
			search_pattern = f"%{searchByName}%"  # Add wildcard characters before and after the search term
			cursor.execute(query, (search_pattern, search_pattern))

			rows = cursor.fetchall()  # Fetch all rows from the query result
			columns = [description[0] for description in cursor.description]  # Get column names
			result = ""
			if not rows:
				result += f"""<tr>
								<td style="text-align:center" colspan="3">No data found</td>
							  </tr>"""
			else:
				# Return the fetched data as a string (for simplicity)
				for row in rows:
					row_data = {columns[i]: row[i] for i in range(len(row))}  # Create dict of column names and row values
					result += f"""<tr>
									<td>{row_data['id']}</td>
									<td>{row_data['firstname']}</td>
									<td>{row_data['lastname']}</td>
								</tr>"""
			
			return {'message': result}
		
		except sqlite3.Error as e:
			return {'message': f"Error: {e}"}
		finally:
			cursor.close()
			connection.close()


def on_loaded():
	window.toggle_fullscreen()


if __name__ == '__main__':
	api = Api()
	
	# Get the path to the HTML file
	current_dir = os.path.dirname(os.path.realpath(__file__))
	html_path = os.path.join(current_dir, 'index.html')

	# Create the window using the external HTML file
	window = webview.create_window('ECO ENEGERY', html_path, js_api=api, width=1000, height=700,)
	webview.start()
