# app/routes.py

from flask import render_template, request, redirect, url_for
from app import app
from manejo_pedidos import ManejoPedidos

manejo_pedidos = ManejoPedidos()

@app.route('/')
def listar_pedidos():
    pedidos = manejo_pedidos.dic_pedidos()
    return render_template('index.html', pedidos=pedidos)

@app.route('/pedido/<int:pedido_id>')
def ver_pedido(pedido_id):
    pedido = manejo_pedidos.ver_pedido(pedido_id)
    return render_template('pedido.html', pedido=pedido)
