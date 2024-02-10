# Requerimientos solicitados
import pymysql.cursors

#Creacion de clase global
class InsertDb:
    #1. Creacion de Productos / Inventario
    def insertProduct(self, connection, data):
        """
        Inserta un nuevo producto en la base de datos.

        Parámetros:
        - connection (pymysql.connections.Connection): Conexión a la base de datos.
        - data (dict): Datos del producto a insertar.

        Retorna:
        - dict: Resultado de la operación.
        """
        try:
            with connection.cursor() as cursor:
                sql = '''INSERT INTO Producto 
                         (idProducto, nombre, sku, precio, compare_precio, cant, imagen) 
                         VALUES (%s, %s, %s, %s, %s, %s, %s);'''
                cursor.execute(sql, (data['idProducto'], data['nombre'], data['sku'], data['precio'], data['compare_precio'], data['cant'], data['imagen']))
            print("Producto insertado correctamente")
            connection.commit()
        except pymysql.IntegrityError as e:
            print(f"Error de integridad al insertar el producto: {e}")
            raise
        except pymysql.Error as e:
            print(f"Error de MySQL al insertar el producto: {e}")
            raise

    #1.1 Consulta de productos
    def getProduct(self, connection, product_id):
        try:
            with connection.cursor() as cursor:
                sql = '''SELECT * FROM Producto WHERE idProducto = %s;'''
                cursor.execute(sql, (product_id,))
                result = cursor.fetchone()
                if result:
                    return {'status': 'success', 'data': result}
                else:
                    return {'status': 'error', 'message': 'Producto no encontrado'}
        except pymysql.Error as e:
            print(f"Error de MySQL al obtener producto por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
        
    #1.2 Actualizacion de productos / Inventario (puntual para modificación de cantidad)
    def updateProduct(self, connection, product_id, data):
        try:
            with connection.cursor() as cursor:
                sql = '''UPDATE Producto SET 
                         nombre = %s, 
                         precio = %s, 
                         compare_precio = %s, 
                         cant = %s,
                         imagen = %s
                         WHERE idProducto = %s;'''
                cursor.execute(sql, (data['nombre'], data['precio'], data['compare_precio'], data['cant'], data['imagen'], product_id))
            print("Producto actualizado correctamente")
            connection.commit()
            return {'status': 'success', 'message': 'Producto actualizado correctamente'}
        except pymysql.Error as e:
            print(f"Error de MySQL al actualizar producto por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
        
    #1.3 Eliminacion de productos
    def deleteProduct(self, connection, product_id):
        try:
            with connection.cursor() as cursor:
                sql = '''DELETE FROM Producto WHERE idProducto = %s;'''
                cursor.execute(sql, (product_id,))
            print("Producto eliminado correctamente")
            connection.commit()
            return {'status': 'success', 'message': 'Producto eliminado correctamente'}
        except pymysql.Error as e:
            print(f"Error de MySQL al eliminar producto por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
        
    #2. Creacion de clientes
    def insertClient(self, connection, data):
        """
        Inserta un nuevo cliente en la base de datos.

        Parámetros:
        - connection (pymysql.connections.Connection): Conexión a la base de datos.
        - data (dict): Datos del cliente a insertar.

        Retorna:
        - dict: Resultado de la operación.
        """
        try:
            with connection.cursor() as cursor:
                sql = '''INSERT INTO Cliente 
                         (idCliente, nombre, documento, email, address, telefono, departamento, ciudad) 
                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'''
                cursor.execute(sql, (data['idCliente'], data['nombre'], data['documento'], data['email'], data['address'], data['telefono'], data['departamento'], data['ciudad']))
            print("Cliente insertado correctamente")
            connection.commit()
        except pymysql.IntegrityError as e:
            print(f"Error de integridad al insertar cliente: {e}")
            raise
        except pymysql.Error as e:
            print(f"Error de MySQL al insertar cliente: {e}")
            raise
        
    #2.1 Consulta de clientes
    def getClient(self, connection, client_id):
        try:
            with connection.cursor() as cursor:
                sql = '''SELECT * FROM Cliente WHERE idCliente = %s;'''
                cursor.execute(sql, (client_id,))
                result = cursor.fetchone()
                if result:
                    return {'status': 'success', 'data': result}
                else:
                    return {'status': 'error', 'message': 'Cliente no encontrado'}
        except pymysql.Error as e:
            print(f"Error de MySQL al obtener cliente por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
       
    #2.2 Actualizacion de datos del cliente
    def updateClient(self, connection, client_id, data):
        try:
            with connection.cursor() as cursor:
                sql = '''UPDATE Cliente SET 
                         email = %s, 
                         address = %s, 
                         telefono = %s, 
                         departamento = %s,
                         ciudad = %s
                         WHERE idCliente = %s;'''
                cursor.execute(sql, (data['email'], data['address'], data['telefono'], data['departamento'], data['ciudad'], client_id))
            print("Cliente actualizado correctamente")
            connection.commit()
            return {'status': 'success', 'message': 'Cliente actualizado correctamente'}
        except pymysql.Error as e:
            print(f"Error de MySQL al actualizar cliente por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
    
    #2.3 Eliminacion del cliente
    def deleteClient(self, connection, client_id):
        try:
            with connection.cursor() as cursor:
                sql = '''DELETE FROM Cliente WHERE idCliente = %s;'''
                cursor.execute(sql, (client_id))
            print("Cliente eliminado correctamente")
            connection.commit()
            return {'status': 'success', 'message': 'Cliente eliminado correctamente'}
        except pymysql.Error as e:
            print(f"Error de MySQL al eliminar cliente por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
    
    #3. Creacion de items
    def insertItem(self, connection, data):
        """
        Inserta un nuevo item en la base de datos.

        Parámetros:
        - connection (pymysql.connections.Connection): Conexión a la base de datos.
        - data (dict): Datos del item a insertar.

        Retorna:
        - dict: Resultado de la operación.
        """
        try:
            with connection.cursor() as cursor:
                sql = '''INSERT INTO items 
                         (iditems, precio_venta, precio_original, cant, descuento, Producto_idProducto, Carrito_idCarrito) 
                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s);'''
                cursor.execute(sql, (data['iditems'], data['precio_venta'], data['precio_original'], data['cant'], data['descuento'], data['Producto_idProducto'], data['Carrito_idCarrito']))
            print("Item insertado correctamente")
            connection.commit()
        except pymysql.IntegrityError as e:
            print(f"Error de integridad al insertar item: {e}")
            raise
        except pymysql.Error as e:
            print(f"Error de MySQL al insertar item: {e}")
            raise
        
    #3.1 Consulta de item
    def getItem(self, connection, item_id):
        try:
            with connection.cursor() as cursor:
                sql = '''SELECT * FROM items WHERE iditems = %s;'''
                cursor.execute(sql, (item_id,))
                result = cursor.fetchone()
                if result:
                    return {'status': 'success', 'data': result}
                else:
                    return {'status': 'error', 'message': 'Item no encontrado'}
        except pymysql.Error as e:
            print(f"Error de MySQL al obtener item por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
       
    #3.2 Actualizacion de datos del item
    def updateItem(self, connection, item_id, data):
        try:
            with connection.cursor() as cursor:
                sql = '''UPDATE items SET 
                         precio_venta = %s, 
                         precio_original = %s, 
                         cant = %s, 
                         descuento = %s
                         WHERE iditems = %s;'''
                cursor.execute(sql, (data['precio_venta'], data['precio_original'], data['cant'], data['descuento'], item_id))
            print("Item actualizado correctamente")
            connection.commit()
            return {'status': 'success', 'message': 'Item actualizado correctamente'}
        except pymysql.Error as e:
            print(f"Error de MySQL al actualizar item por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
    
    #3.3 Eliminacion del item
    def deleteItem(self, connection, item_id):
        try:
            with connection.cursor() as cursor:
                sql = '''DELETE FROM items WHERE iditem = %s;'''
                cursor.execute(sql, (item_id))
            print("Item eliminado correctamente")
            connection.commit()
            return {'status': 'success', 'message': 'Item eliminado correctamente'}
        except pymysql.Error as e:
            print(f"Error de MySQL al eliminar item por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
    
    #4. Creacion de carrito
    def insertCar(self, connection, data):
        """
        Inserta un nuevo carrito en la base de datos.

        Parámetros:
        - connection (pymysql.connections.Connection): Conexión a la base de datos.
        - data (dict): Datos del carrito a insertar.

        Retorna:
        - dict: Resultado de la operación.
        """
        try:
            with connection.cursor() as cursor:
                sql = '''INSERT INTO Carrito 
                         (idCarrito, descuento, total, subtotal) 
                         VALUES (%s, %s, %s, %s);'''
                cursor.execute(sql, (data['idCarrito'], data['descuento'], data['total'], data['subtotal']))
            print("Carrito insertado correctamente")
            connection.commit()
        except pymysql.IntegrityError as e:
            print(f"Error de integridad al insertar carrito: {e}")
            raise
        except pymysql.Error as e:
            print(f"Error de MySQL al insertar carrito: {e}")
            raise
        
    #4.1 Consulta de carrito
    def getCar(self, connection, car_id):
        try:
            with connection.cursor() as cursor:
                sql = '''SELECT * FROM Carrito WHERE idCarrito = %s;'''
                cursor.execute(sql, (car_id,))
                result = cursor.fetchone()
                if result:
                    return {'status': 'success', 'data': result}
                else:
                    return {'status': 'error', 'message': 'Carrito no encontrado'}
        except pymysql.Error as e:
            print(f"Error de MySQL al obtener carrito por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
       
    #4.2 Actualizacion de datos del carrito
    def updateCar(self, connection, car_id, data):
        try:
            with connection.cursor() as cursor:
                sql = '''UPDATE Carrito SET 
                         descuento = %s, 
                         total = %s, 
                         subtotal = %s
                         WHERE idCarrito = %s;'''
                cursor.execute(sql, (data['descuento'], data['total'], data['subtotal'], car_id))
            print("Carrito actualizado correctamente")
            connection.commit()
            return {'status': 'success', 'message': 'Carrito actualizado correctamente'}
        except pymysql.Error as e:
            print(f"Error de MySQL al actualizar carrito por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
    
    #4.3 Eliminacion del carrito
    def deleteCar(self, connection, car_id):
        try:
            with connection.cursor() as cursor:
                sql = '''DELETE FROM Carrito WHERE idCarrito = %s;'''
                cursor.execute(sql, (car_id))
            print("Carrito eliminado correctamente")
            connection.commit()
            return {'status': 'success', 'message': 'Carrito eliminado correctamente'}
        except pymysql.Error as e:
            print(f"Error de MySQL al eliminar carrito por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
    
    #5. Creacion de orden
    def insertOrder(self, connection, data):
        """
        Inserta una nueva orden en la base de datos.

        Parámetros:
        - connection (pymysql.connections.Connection): Conexión a la base de datos.
        - data (dict): Datos de la orden a insertar.

        Retorna:
        - dict: Resultado de la operación.
        """
        try:
            with connection.cursor() as cursor:
                sql = '''INSERT INTO Orden 
                         (OrdenId, numero_orden, Cliente_idCliente, Carrito_idCarrito, Metodos de envio_idMetodos de envio, Metodos de pago_idMetodos de pago) 
                         VALUES (%s, %s, %s, %s);'''
                cursor.execute(sql, (data['OrdenId'],data['numero_orden'],data['Cliente_idCliente'], data['Carrito_idCarrito'], data['Metodos de envio_idMetodos de envio'], data['Metodos de pago_idMetodos de pago']))
            print("Orden insertada correctamente")
            connection.commit()
        except pymysql.IntegrityError as e:
            print(f"Error de integridad al insertar orden: {e}")
            raise
        except pymysql.Error as e:
            print(f"Error de MySQL al insertar orden: {e}")
            raise
        
    #5.1 Consulta de orden
    def getOrder(self, connection, order_id):
        try:
            with connection.cursor() as cursor:
                sql = '''SELECT * FROM Orden WHERE OrdenId = %s;'''
                cursor.execute(sql, (order_id))
                result = cursor.fetchone()
                if result:
                    return {'status': 'success', 'data': result}
                else:
                    return {'status': 'error', 'message': 'Orden no encontrada'}
        except pymysql.Error as e:
            print(f"Error de MySQL al obtener orden por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
       
    #5.2 Actualizacion de datos de la orden
    def updateOrder(self, connection, order_id, data):
        try:
            with connection.cursor() as cursor:
                sql = '''UPDATE Orden SET 
                         numero_orden = %s
                         WHERE OrdenId = %s;'''
                cursor.execute(sql, (data['numero_orden'], order_id))
            print("Orden actualizada correctamente")
            connection.commit()
            return {'status': 'success', 'message': 'Orden actualizada correctamente'}
        except pymysql.Error as e:
            print(f"Error de MySQL al actualizar orden por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
    
    #5.3 Eliminacion de la orden
    def deleteOrder(self, connection, order_id):
        try:
            with connection.cursor() as cursor:
                sql = '''DELETE FROM Orden WHERE OrdenId = %s;'''
                cursor.execute(sql, (order_id))
            print("Orden eliminada correctamente")
            connection.commit()
            return {'status': 'success', 'message': 'Orden eliminada correctamente'}
        except pymysql.Error as e:
            print(f"Error de MySQL al eliminar orden por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
        
    #6. Creacion de métodos de envío
    def insertShippingMethod(self, connection, data):
        """
        Inserta un nuevo metodo de envio en la base de datos.

        Parámetros:
        - connection (pymysql.connections.Connection): Conexión a la base de datos.
        - data (dict): Datos del metodo de envio a insertar.

        Retorna:
        - dict: Resultado de la operación.
        """
        try:
            with connection.cursor() as cursor:
                sql = '''INSERT INTO Metodos de envio 
                         (idMetodos de envio, nombre, valor) 
                         VALUES (%s, %s, %s);'''
                cursor.execute(sql, (data['idMetodos de envio'],data['nombre'],data['valor']))
            print("Metodo de envio insertado correctamente")
            connection.commit()
        except pymysql.IntegrityError as e:
            print(f"Error de integridad al insertar metodo de envio: {e}")
            raise
        except pymysql.Error as e:
            print(f"Error de MySQL al insertar metodo de envio: {e}")
            raise
        
    #6.1 Consulta de metodo de envio
    def getShippingMethod(self, connection, shipping_id):
        try:
            with connection.cursor() as cursor:
                sql = '''SELECT * FROM Metodos de envio WHERE idMetodos de envio = %s;'''
                cursor.execute(sql, (shipping_id))
                result = cursor.fetchone()
                if result:
                    return {'status': 'success', 'data': result}
                else:
                    return {'status': 'error', 'message': 'Metodo de envio no encontrado'}
        except pymysql.Error as e:
            print(f"Error de MySQL al obtener metodo de envio por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
       
    #6.2 Actualizacion de datos del metodo de envio
    def updateShippingMethod(self, connection, shipping_id, data):
        try:
            with connection.cursor() as cursor:
                sql = '''UPDATE Metodos de envio SET 
                         nombre = %s,
                         valor = %s
                         WHERE idMetodos de envio = %s;'''
                cursor.execute(sql, (data['nombre'], data['valor'], shipping_id))
            print("Metodo de envio actualizado correctamente")
            connection.commit()
            return {'status': 'success', 'message': 'Metodo de envio actualizado correctamente'}
        except pymysql.Error as e:
            print(f"Error de MySQL al actualizar metodo de envio por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
    
    #6.3 Eliminacion del metodo de envio
    def deleteShippingMethod(self, connection, shipping_id):
        try:
            with connection.cursor() as cursor:
                sql = '''DELETE FROM Metodos de envio WHERE idMetodos de envio = %s;'''
                cursor.execute(sql, (shipping_id))
            print("Metodo de envio eliminado correctamente")
            connection.commit()
            return {'status': 'success', 'message': 'Metodo de envio eliminado correctamente'}
        except pymysql.Error as e:
            print(f"Error de MySQL al eliminar metodo de envio por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
        

    #7. Creacion de métodos de pago
    def insertPaymentMethod(self, connection, data):
        """
        Inserta un nuevo metodo de pago en la base de datos.

        Parámetros:
        - connection (pymysql.connections.Connection): Conexión a la base de datos.
        - data (dict): Datos del metodo de pago a insertar.

        Retorna:
        - dict: Resultado de la operación.
        """
        try:
            with connection.cursor() as cursor:
                sql = '''INSERT INTO Metodos de pago 
                         (idMetodos de pago, nombre) 
                         VALUES (%s, %s, %s);'''
                cursor.execute(sql, (data['idMetodos de pago'],data['nombre']))
            print("Metodo de pago insertado correctamente")
            connection.commit()
        except pymysql.IntegrityError as e:
            print(f"Error de integridad al insertar metodo de pago: {e}")
            raise
        except pymysql.Error as e:
            print(f"Error de MySQL al insertar metodo de pago: {e}")
            raise
        
    #7.1 Consulta de metodo de pago
    def getPaymentMethod(self, connection, payment_id):
        try:
            with connection.cursor() as cursor:
                sql = '''SELECT * FROM Metodos de pago WHERE idMetodos de pago = %s;'''
                cursor.execute(sql, (payment_id))
                result = cursor.fetchone()
                if result:
                    return {'status': 'success', 'data': result}
                else:
                    return {'status': 'error', 'message': 'Metodo de pago no encontrado'}
        except pymysql.Error as e:
            print(f"Error de MySQL al obtener metodo de pago por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
       
    #7.2 Actualizacion de datos del metodo de pago
    def updatePaymentMethod(self, connection, payment_id, data):
        try:
            with connection.cursor() as cursor:
                sql = '''UPDATE Metodos de pago SET 
                         nombre = %s
                         WHERE idMetodos de pago = %s;'''
                cursor.execute(sql, (data['nombre'], data['valor'], payment_id))
            print("Metodo de pago actualizado correctamente")
            connection.commit()
            return {'status': 'success', 'message': 'Metodo de pago actualizado correctamente'}
        except pymysql.Error as e:
            print(f"Error de MySQL al actualizar metodo de pago por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
    
    #7.3 Eliminacion del metodo de pago
    def deletePaymentMethod(self, connection, payment_id):
        try:
            with connection.cursor() as cursor:
                sql = '''DELETE FROM Metodos de pago WHERE idMetodos de pago = %s;'''
                cursor.execute(sql, (payment_id))
            print("Metodo de pago eliminado correctamente")
            connection.commit()
            return {'status': 'success', 'message': 'Metodo de pago eliminado correctamente'}
        except pymysql.Error as e:
            print(f"Error de MySQL al eliminar metodo de pago por ID: {e}")
            return {'status': 'error', 'message': f'Error de MySQL: {e}'}
    
    #8 Lista de ordenes, segun relaciones con tablas 
    def getOrderList(self, connection, order_id):
        try:
            with connection.cursor() as cursor:
                # Consulta para obtener la orden por ID
                sql_order = '''SELECT * FROM Orden WHERE OrdenId = %s;'''
                cursor.execute(sql_order, (order_id))
                order_result = cursor.fetchone()

                if order_result:
                    # Información de la orden
                    order_data = {
                        'OrdenId': order_result['OrdenId'],
                        'numero_orden': order_result['numero_orden'],
                        'Cliente_idCliente': order_result['Cliente_idCliente'],
                        'Metodos de envio_idMetodos de envio': order_result['Metodos de envio_idMetodos de envio'],
                        'Metodos de pago_idMetodos de pago': order_result['Metodos de pago_idMetodos de pago']
                    }

                    # Consulta para obtener información del cliente
                    sql_cliente = '''SELECT * FROM Cliente WHERE idCliente = %s;'''
                    cursor.execute(sql_cliente, (order_data['Cliente_idCliente']))
                    cliente_result = cursor.fetchone()
                    order_data['cliente'] = cliente_result

                    # Consulta para obtener información del método de envío
                    sql_metodo_envio = '''SELECT * FROM `Metodos de envio` WHERE `idMetodos de envio` = %s;'''
                    cursor.execute(sql_metodo_envio, (order_data['Metodos de envio_idMetodos de envio']))
                    metodo_envio_result = cursor.fetchone()
                    order_data['metodo_envio'] = metodo_envio_result

                    # Consulta para obtener información del método de pago
                    sql_metodo_pago = '''SELECT * FROM `Metodos de pago` WHERE `idMetodos de pago` = %s;'''
                    cursor.execute(sql_metodo_pago, (order_data['Metodos de pago_idMetodos de pago']))
                    metodo_pago_result = cursor.fetchone()
                    order_data['metodo_pago'] = metodo_pago_result

                    return {'status': 'success', 'data': order_data}
                else:
                    return {'status': 'error', 'message': 'Orden no encontrada'}
        except pymysql.Error as e:
            print(f"Error de MySQL al obtener orden por ID: {e}")
        return {'status': 'error', 'message': f'Error de MySQL: {e}'}
    
    
 