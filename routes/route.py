# Rutas para ejecución en Flask
from flask import Blueprint, Flask, jsonify, request
import pymysql
from BD.connection import NataBD
from requirements.req import InsertDb

# Creación de un Blueprint llamado "Api"
Api = Blueprint("Api", __name__)

# Ruta para insertar un producto (en body)
@Api.route("/insertProduct", methods=['POST'])
def insertProduct():
    try:
        data = request.get_json()
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            result = InsertDb().insertProduct(connectionNat, data)
            return jsonify({"success": True})
        
    except Exception as e:
        print(e)
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para obtener datos de un producto por ID (en parametros)
@Api.route("/getProduct/<int:product_id>", methods=['GET'])
def getProduct(product_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            data = InsertDb().getProduct(connectionNat, product_id)

        if data.get('status') == 'success':
            return jsonify(data)
        else:
            return jsonify(data), 500

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para actualizar datos de un producto por ID (ID en parametros, informacion a modificar en body)
@Api.route("/updateProduct/<int:product_id>", methods=['PUT'])
def updateProduct(product_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()
        
        data = request.json 
        
        with connectionNat:
            result = InsertDb().updateProduct(connectionNat, product_id, data)

        return jsonify(result)

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para eliminar un producto por ID (en parametros)
@Api.route("/deleteProduct/<int:product_id>", methods=['DELETE'])
def deleteProduct(product_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            result = InsertDb().deleteProduct(connectionNat, product_id)

        return jsonify(result)

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para insertar un cliente (en body)
@Api.route("/insertClient", methods=['POST'])
def insertClient():
    try:
        data = request.get_json()
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            result = InsertDb().insertClient(connectionNat, data)

        return jsonify({"success": True})

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para obtener datos de un cliente por ID (en parametros)
@Api.route("/getClient/<int:client_id>", methods=['GET'])
def getClient(client_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            result = InsertDb().getClient(connectionNat, client_id)

        if result.get('status') == 'success':
            return jsonify(result)
        else:
            return jsonify(result), 500

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para actualizar datos de un cliente por ID (ID en parametros, informacion a modificar en body)
@Api.route("/updateClient/<int:client_id>", methods=['PUT'])
def updateClient(client_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()
        
        data = request.json
        
        with connectionNat:
            result = InsertDb().updateClient(connectionNat, client_id, data)

        return jsonify(result)

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para eliminar un cliente por ID (en parametros)
@Api.route("/deleteClient/<int:client_id>", methods=['DELETE'])
def deleteClient(client_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            result = InsertDb().deleteClient(connectionNat, client_id)

        return jsonify(result)

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500







# Ruta para insertar un item (en body)
@Api.route("/insertItem", methods=['POST'])
def insertItem():
    try:
        data = request.get_json()
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            result = InsertDb().insertItem(connectionNat, data)
            return jsonify({"success": True})
        
    except Exception as e:
        print(e)
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para obtener datos de un item por ID (en parametros)
@Api.route("/getItem/<int:item_id>", methods=['GET'])
def getItem(item_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            data = InsertDb().getItem(connectionNat, item_id)

        if data.get('status') == 'success':
            return jsonify(data)
        else:
            return jsonify(data), 500

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para actualizar datos de un item por ID (ID en parametros, informacion a modificar en body)
@Api.route("/updateItem/<int:item_id>", methods=['PUT'])
def updateItem(item_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()
        
        data = request.json 
        
        with connectionNat:
            result = InsertDb().updateItem(connectionNat, item_id, data)

        return jsonify(result)

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para eliminar un producto por ID (en parametros)
@Api.route("/deleteItem/<int:item_id>", methods=['DELETE'])
def deleteItem(item_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            result = InsertDb().deleteItem(connectionNat, item_id)

        return jsonify(result)

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para insertar un carrito (en body)
@Api.route("/insertCar", methods=['POST'])
def insertCar():
    try:
        data = request.get_json()
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            result = InsertDb().insertCar(connectionNat, data)

        return jsonify({"success": True})

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para obtener datos de un carrito por ID (en parametros)
@Api.route("/getCar/<int:car_id>", methods=['GET'])
def getCar(car_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            result = InsertDb().getCar(connectionNat, car_id)

        if result.get('status') == 'success':
            return jsonify(result)
        else:
            return jsonify(result), 500

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para actualizar datos de un carrito por ID (ID en parametros, informacion a modificar en body)
@Api.route("/updateCar/<int:car_id>", methods=['PUT'])
def updateCar(car_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()
        
        data = request.json
        
        with connectionNat:
            result = InsertDb().updateCar(connectionNat, car_id, data)

        return jsonify(result)

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para eliminar un carrito por ID (en parametros)
@Api.route("/deleteCar/<int:car_id>", methods=['DELETE'])
def deleteCar(car_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            result = InsertDb().deleteCar(connectionNat, car_id)

        return jsonify(result)

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500









# Ruta para insertar una orden (en body)
@Api.route("/insertOrder", methods=['POST'])
def insertOrder():
    try:
        data = request.get_json()
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            result = InsertDb().insertOrder(connectionNat, data)
            return jsonify({"success": True})
        
    except Exception as e:
        print(e)
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para obtener datos de una orden por ID (en parametros)
@Api.route("/getOrder/<int:order_id>", methods=['GET'])
def getOrder(order_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            data = InsertDb().getOrder(connectionNat, order_id)

        if data.get('status') == 'success':
            return jsonify(data)
        else:
            return jsonify(data), 500

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para actualizar datos de una orden por ID (ID en parametros, informacion a modificar en body)
@Api.route("/updateOrder/<int:order_id>", methods=['PUT'])
def updateOrder(order_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()
        
        data = request.json 
        
        with connectionNat:
            result = InsertDb().updateOrder(connectionNat, order_id, data)

        return jsonify(result)

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para eliminar una orden por ID (en parametros)
@Api.route("/deleteOrder/<int:order_id>", methods=['DELETE'])
def deleteOrder(order_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            result = InsertDb().deleteOrder(connectionNat, order_id)

        return jsonify(result)

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para insertar un metodo de envio (en body)
@Api.route("/insertShippingMethod", methods=['POST'])
def insertShippingMethod():
    try:
        data = request.get_json()
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            result = InsertDb().insertShippingMethod(connectionNat, data)

        return jsonify({"success": True})

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para obtener datos de un metodo de envio por ID (en parametros)
@Api.route("/getShippingMethod/<int:shipping_id>", methods=['GET'])
def getShippingMethod(shipping_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            result = InsertDb().getShippingMethod(connectionNat, shipping_id)

        if result.get('status') == 'success':
            return jsonify(result)
        else:
            return jsonify(result), 500

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para actualizar datos de un metodo de envio por ID (ID en parametros, informacion a modificar en body)
@Api.route("/updateShippingMethod/<int:shipping_id>", methods=['PUT'])
def updateShippingMethod(shipping_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()
        
        data = request.json
        
        with connectionNat:
            result = InsertDb().updateShippingMethod(connectionNat, shipping_id, data)

        return jsonify(result)

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para eliminar un metodo de envio por ID (en parametros)
@Api.route("/deleteShippingMethod/<int:shipping_id>", methods=['DELETE'])
def deleteShippingMethod(shipping_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            result = InsertDb().deleteShippingMethod(connectionNat, shipping_id)

        return jsonify(result)

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para insertar un metodo de pago (en body)
@Api.route("/insertPaymentMethod", methods=['POST'])
def insertPaymentMethod():
    try:
        data = request.get_json()
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            result = InsertDb().insertPaymentMethod(connectionNat, data)

        return jsonify({"success": True})

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para obtener datos de un metodo de envio por ID (en parametros)
@Api.route("/getPaymentMethod/<int:payment_id>", methods=['GET'])
def getPaymentMethod(payment_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            result = InsertDb().getPaymentMethod(connectionNat, payment_id)

        if result.get('status') == 'success':
            return jsonify(result)
        else:
            return jsonify(result), 500

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para actualizar datos de un metodo de pago por ID (ID en parametros, informacion a modificar en body)
@Api.route("/updatePaymentMethod/<int:payment_id>", methods=['PUT'])
def updatePaymentMethod(payment_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()
        
        data = request.json
        
        with connectionNat:
            result = InsertDb().updatePaymentMethod(connectionNat, payment_id, data)

        return jsonify(result)

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500

# Ruta para eliminar un metodo de envio por ID (en parametros)
@Api.route("/deletePaymentMethod/<int:payment_id>", methods=['DELETE'])
def deletePaymentMethod(payment_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            result = InsertDb().deletePaymentMethod(connectionNat, payment_id)

        return jsonify(result)

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500
    
    # Ruta para obtener datos de la lista de orden por ID (en parametros)
@Api.route("/getOrderList/<int:order_id>", methods=['GET'])
def getOrderList(order_id):
    try:
        dbLocal = NataBD(conectionType='NAT')
        connectionNat = dbLocal.getConection()

        with connectionNat:
            result = InsertDb().getOrderList(connectionNat, order_id)

        if result.get('status') == 'success':
            return jsonify(result)
        else:
            return jsonify(result), 500

    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Error: {e}'}), 500