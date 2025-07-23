# Procesos linux

[VER AMPLIADO file:///home/daniel/tron/1-LEGOS/GNU-LINUX/Ubuntu20.04JammyLts/PROCESOS/bg%20&%20disown%20setsid%20%20Separar%20por%20completo%20un%20proceso%20de%20la%20terminal%20_%20Baldung%20en%20Linux-www.baeldung.com.mhtml](file:///home/daniel/tron/1-LEGOS/GNU-LINUX/Ubuntu20.04JammyLts/PROCESOS/bg%20&%20disown%20setsid%20%20Separar%20por%20completo%20un%20proceso%20de%20la%20terminal%20_%20Baldung%20en%20Linux-www.baeldung.com.mhtml)

## Repudiar

* Cuando ejecutamos un comando con  setsid , el comando se inicia en una nueva sesión que se desconecta de la terminal actual. Similar a rechazar y usar " & ", la salida se imprime en la terminal actual y podemos silenciarla enviándola a  /dev/null :
  
  ```bash
  
  ```



```
## Registrar Proceso en Script y Matarlo:

1 Para registrar un proceso dentro del Script:
El proceso se registra y se exporta como variables globales:

NUMERO_PID
NOMBRE_PID

``` bash
source $programas/sesiones/sesiones/procesos.sh
id_proceso=$!
nombre_proceso="mkdocs"
registraProceso $nombre_proceso $id_proceso
```

2 Matarlo:

```bash
# $1 recibe la forma de cierre [nombre/numero/todos]
# $2 recibe el nombre_proceso ó num_proceso 
# Ejemplo de la función:

cierraProceso nombre mkdocs
cierraProceso numero 9767
cierraProceso todos
```

## Procesos en puertos y sockets:

```bash
# Para saber que proceso se ejecuta en el puerto 8000 (el de mkdocs)

fuser 8000/tcp

# Para matar el proceso en el puerto 8000

fuser -k 8000/tcp
```

¡Claro! Vamos a explorar algunos conceptos relacionados con la gestión de procesos en Linux, junto con ejemplos prácticos:

1. **Foreground y Background**:
   
   - **Foreground**: Cuando ejecutas un comando en la terminal, normalmente se ejecuta en primer plano (foreground). Esto significa que el comando ocupa la terminal y debes esperar a que termine antes de ejecutar otro.
   - **Background**: Puedes enviar un comando al segundo plano (background) agregando un `&` al final. De esta manera, puedes liberar la terminal para ejecutar otros comandos mientras el proceso sigue en ejecución.
   
   Ejemplo:
   
   ```bash
   sleep 10  # Espera 10 segundos (en primer plano)
   sleep 10 &  # Espera 10 segundos (en segundo plano)
   ```

2. **bg, fg y jobs**:
   
   - `bg`: Mueve un proceso suspendido al segundo plano.
   - `fg`: Trae un proceso en segundo plano al primer plano.
   - `jobs`: Lista los procesos en segundo plano.
   
   Ejemplo:
   
   ```bash
   # Ejecutar un proceso en segundo plano
   gedit &
   
   # Ver los procesos en segundo plano
   jobs
   
   # Traer un proceso al primer plano
   fg %1  # Donde 1 es el número de trabajo mostrado por "jobs"
   ```

3. **& (Ampersand)**:
   
   - Agregar `&` al final de un comando lo ejecuta en segundo plano.
   
   Ejemplo:
   
   ```bash
   gedit &  # Abre el editor de texto Gedit en segundo plano
   ```

4. **nohup**:
   
   - Ejecuta un comando incluso después de cerrar la terminal o la sesión SSH.
   - Útil para procesos largos o tareas en segundo plano.
   
   Ejemplo:
   
   ```bash
   nohup long_running_command > output.log &
   ```

5. **disown**:
   
   - Desvincula un proceso del terminal actual.
   - Útil para evitar que un proceso se detenga cuando cierras la terminal.
   
   Ejemplo:
   
   ```bash
   gedit &  # Abre Gedit en segundo plano
   disown %1  # Desvincula el proceso de Gedit
   ```

6. **setsid**:
   
   - Crea un nuevo grupo de procesos independiente.
   - Útil para ejecutar procesos sin conexión con la terminal actual.
   
   Ejemplo:
   
   ```bash
   setsid long_running_command
   ```

7. **screen**:
   
   - Crea sesiones de terminal virtuales independientes.
   - Útil para mantener procesos en ejecución incluso después de cerrar la sesión.
   
   Ejemplo:
   
   ```bash
   screen  # Inicia una nueva sesión de screen
   long_running_command  # Ejecuta un proceso
   Ctrl+A, D  # Desconecta la sesión de screen
   screen -r  # Reanuda la sesión de screen
   ```

¡Espero que esta explicación te ayude a comprender mejor la gestión de procesos en Linux! 😊



# Separe completamente un proceso de la terminal

Última modificación: 6 de junio de 2022

Escrito por: [Karthik Devan](https://www.baeldung.com/linux/author/karthikdevan "Posts by Karthik Devan")[](https://www.baeldung.com/linux/author/karthikdevan "Mensajes de Karthik Devan")

- [Procesos](https://www.baeldung.com/linux/category/processes)

- [bg](https://www.baeldung.com/linux/tag/bg)
   - [fg](https://www.baeldung.com/linux/tag/fg)
   - [trabajos](https://www.baeldung.com/linux/tag/jobs)
   - [Nohup](https://www.baeldung.com/linux/tag/nohup)
   - [pantalla](https://www.baeldung.com/linux/tag/screen)

Si tiene algunos años de experiencia en el ecosistema de Linux y está interesado en compartir esa experiencia con la comunidad, consulte nuestras [**Pautas de contribución**](https://www.baeldung.com/linux/contribution-guidelines) .

## 1. Introducción[](https://www.baeldung.com/linux/detach-process-from-terminal#introduction)

As Linux users, we often use the terminal to run various commands and programs. We run commands that take more than just a moment to complete in various scenarios. In such cases, we may want to run the command in the background so the terminal is free for other work. Or, we may be running the command remotely in an [SSH](https://www.baeldung.com/cs/ssh-intro) session, in which case we can conveniently start the process in the background and exit the session after that.

In this tutorial, **we’ll look at several ways to detach a process from the terminal entirely.** We can use some methods to start the process in the background, while some methods help us move an already running process to the background.

## 2. Using *bg*, *fg*, and *jobs*[](https://www.baeldung.com/linux/detach-process-from-terminal#usingbg-fg-and-jobs)

Once a command has started running, **we can hit *Ctrl+Z* to freeze the process and then use the [*bg*](https://man7.org/linux/man-pages/man1/bg.1p.html) command to resume it in the background.** We can then use the [*jobs*](https://man7.org/linux/man-pages/man1/jobs.1p.html) command to view the running backgrounded processes:

```bash
$ sleep 10
^Z
[1]+  Stopped                 sleep 10
$ bg
[1]+ sleep 10 &
$ jobs
[1]+  Running                 sleep 10 &
$ echo

[1]+  Done                    sleep 10
```

The above snippet shows the output for a process stopped with *Ctrl+Z* and then moved to the background with *bg.* Running the *jobs* command tells us that the previous command is indeed still running but in the background. Running another random command (*echo*) after 10 seconds tells us that the initial command has been completed.

Una vez que movemos un proceso al fondo usando el  comando *bg* , es posible **traerlo de vuelta al primer plano usando el comando [*fg :*](https://man7.org/linux/man-pages/man1/fg.1p.html)**

```bash
$ (sleep 11 && echo hello)
^Z
[1]+  Stopped                 ( sleep 11 && echo hello )
$ bg
[1]+ ( sleep 11 && echo hello ) &
$ fg
( sleep 11 && echo hello )
hello
```

En el fragmento anterior, se supone que el comando inicial debe esperar 11 segundos e imprimir "hola". Después de enviarlo al fondo y traerlo de vuelta al primer plano usando  *fg,* vemos que el comando imprime "hola" en el primer plano.

## 3. Uso del operador &[](https://www.baeldung.com/linux/detach-process-from-terminal#using-the-amp-operator)

Podemos **iniciar un comando en segundo plano agregando " *&"* al final** del comando:

```shell
$ gedit &
[1] 968967
$ 
(gedit:968967): GtkSourceView-WARNING **: 16:15:38.174: could not parse color '#bg'

(gedit:968967): GtkSourceView-WARNING **: 16:15:38.175: no color named 'white'
$ echo "running another command"
running another command
$ kill 968967
```

De lo anterior, vemos que agregar un ampersand al  comando *gedit* lo envía al fondo e imprime su PID, 968967. Gedit es un programa GUI y se abre en el escritorio mientras deja la terminal libre para ejecutar otros comandos. Cuando ejecutamos el comando [*kill*](https://www.baeldung.com/linux/kill-commands) en su PID, el programa sale.

También vemos que la salida del  comando *gedit* aún se imprime en este terminal. Para evitar eso, podemos redirigir la salida a otra ubicación, digamos  *[/dev/null](https://www.baeldung.com/linux/silencing-bash-output)* :

```bash
$ gedit 1>/dev/null 2>/dev/null &
[1] 979813
$ kill 979813
$ echo "hello"
hello
[1]+  Terminated              gedit > /dev/null 2> /dev/null
```

En este caso, redirigimos los flujos de salida y error a */dev/null,* y ahora se suprime la salida que vimos anteriormente. Como resultado, solo recibimos una notificación del PID en nuestro terminal inicialmente y luego solo cuando el proceso ha finalizado.

## 4. Usar  *nohup*[](https://www.baeldung.com/linux/detach-process-from-terminal#usingnohup)

**El  comando [*nohup*](https://man7.org/linux/man-pages/man1/nohup.1.html) se usa para ejecutar un comando de una manera que es inmune a "colgaduras" o desconexiones de terminales.** Cuando iniciamos un comando usando *nohup,* el comando redirige la salida a *nohup.out* :

```bash
$ nohup echo hello &
[1] 998797
nohup: ignoring input and appending output to 'nohup.out'
$
^C
[1]+  Done                    nohup echo hello
$ cat nohup.out
hello
```

En el fragmento anterior, comenzamos un comando usando  *nohup* , agregando "&" al final, por lo que el terminal puede ejecutar otros comandos. Una vez que se completa el proceso, encontramos la salida del comando en el  archivo *nohup.out* .

## 5. Usar  *repudiar*[](https://www.baeldung.com/linux/detach-process-from-terminal#usingdisown)

Podemos ejecutar un comando y **hacer que el terminal rechace el proceso agregando " *& [disown](https://linuxcommand.org/lc3_man_pages/disownh.html) "*** al final:

```bash
$ echo hello & disown
[1] 1007802
hello
```

Después de desautorizar, vemos que el comando imprime primero el PID, seguido de la salida del programa, que aún aparece en nuestra terminal. Para silenciar la salida, podemos redirigirla a */dev/null,*  como hicimos antes:

```bash
$ echo hello 1>/dev/null 2>/dev/null & disown
[1] 1016729
```

Ahora, el comando imprime solo el PID y no la salida del comando.

## 6. Uso  *del sitio*[](https://www.baeldung.com/linux/detach-process-from-terminal#usingsetsid)

Cuando **ejecutamos un comando con  [*setsid*](https://man7.org/linux/man-pages/man2/setsid.2.html) , el comando se inicia en una nueva sesión que se desconecta de la terminal actual.** Similar a rechazar y usar " *&* ", la salida se imprime en la terminal actual y podemos silenciarla enviándola a  */dev/null* :

```bash
$ setsid echo hello
hello
$ setsid echo hello 1>/dev/null 2>/dev/null
```

En el último caso, el comando no imprime ningún resultado en el terminal.

## 7. Uso *de la pantalla*[](https://www.baeldung.com/linux/detach-process-from-terminal#using-screen)

[*Screen*](https://www.baeldung.com/linux/screen-command) es un gestor de ventanas que nos permite iniciar y gestionar múltiples terminales virtuales. **Para ejecutar un proceso en segundo plano usando  *screen* , podemos crear una nueva ventana, iniciar el proceso allí y separar la ventana.**

### 7.1. Entrar en una ventana de pantalla[](https://www.baeldung.com/linux/detach-process-from-terminal#1-entering-a-screen-window)

Para ingresar a una nueva ventana de pantalla, simplemente escribimos el  comando *de pantalla* :

```bash
$ screen
[screen_window] $ 
```

Una vez que estemos dentro, podemos presionar  *Ctrl+A* seguido de ” (comillas dobles) para listar todas las ventanas de pantalla activas:

```bash
[screen_window] 
Ctrl+A "  Num Name    0 bash
```

Vemos que solo hay una ventana de pantalla. Tenga en cuenta que "[screen_window]" se muestra en los fragmentos de código solo para diferenciarlo del terminal original, y en realidad no se imprime en la salida.

### 7.2. Iniciar un comando en la ventana de pantalla[](https://www.baeldung.com/linux/detach-process-from-terminal#2-start-a-command-in-the-screen-window)

Ahora comencemos un comando de larga ejecución dentro de nuestra ventana de pantalla:

```bash
$ watch -n 1 date
```

This will show output similar to below that continuously refreshes itself every second until we exit using *Ctrl+C:*

```bash
Every 1.0s: date                          dell: Thu Jun  2 17:13:14 2022

Thursday 02 June 2022 05:13:14 PM IST
```

### 7.3. Detach From the Screen Window[](https://www.baeldung.com/linux/detach-process-from-terminal#3-detach-from-the-screen-window)

Now, we can detach from this screen window and go back to our original terminal session by pressing *Ctrl+A* followed by *d:*

```bash
[screen_window}
Ctrl+A d
$ screen
[detached from 1045567.pts-1.dell] 
```

When we return to the original terminal, we see the screen command we typed earlier. We also see some new output below, which says we detached from a screen window and got back here.

### 7.4. Go Back to the Screen Window[](https://www.baeldung.com/linux/detach-process-from-terminal#4-go-back-to-the-screen-window)

We can re-enter our screen window by running *screen* with the *-R* flag:

```bash
$ screen -R
[screen_window]
Every 1.0s: date                     dell: Thu Jun  2 17:23:05 2022

Thursday 02 June 2022 05:23:05 PM IST
```

We see that the *watch* command we started earlier is still running inside this screen window.

### 7.5. Exit the Screen Window[](https://www.baeldung.com/linux/detach-process-from-terminal#5-exit-the-screen-window)

To exit this screen window, we can press *Ctrl+C* to stop the process. Then, use the [*exit*](https://man7.org/linux/man-pages/man3/exit.3.html) command to close the window:

```bash
[screen_window]
Ctrl+C
[screen_window] $ exit

$ screen -R
[screen is terminating]
```

After exiting the screen window, we go back to the original terminal. Here, we see the *screen -R* command we previously ran, along with output that says *screen* is terminating.

## 8. Using *pm2*[](https://www.baeldung.com/linux/detach-process-from-terminal#usingpm2)

**For cases when we need to detach a program from the terminal and keep it running forever, we can use a program called [*pm2*](https://pm2.io/docs/runtime/reference/pm2-cli/).** This is best suited for running application servers or bots that need to be online 24×7 and automatically restart if a crash occurs. *Pm2* takes care of all that.

### 8.1. Installing *pm2*[](https://www.baeldung.com/linux/detach-process-from-terminal#1-installingpm2)

Before installing *pm2,* we need to ensure that we have *nodejs* and *npm* installed by running the following commands:

```bash
$ node -v
v14.18.1
$ npm -v
6.14.15
```

Then we can install *pm2*:

```shell
$ sudo npm install -g pm2
```

### 8.2. Running Programs With *pm2*[](https://www.baeldung.com/linux/detach-process-from-terminal#2-running-programs-withpm2)

We can start a *nodejs* program with *pm2* using *pm2 start:*

```bash
$ pm2 start test.js
[PM2] Spawning PM2 daemon with pm2_home=/home/kd/.pm2
[PM2] PM2 Successfully daemonized
[PM2] Starting /home/kd/tinkering/test.js in fork_mode (1 instance)
[PM2] Done.
┌────┬────────────────────┬──────────┬──────┬───────────┬──────────┬──────────┐
│ id │ name               │ mode     │ ↺    │ status    │ cpu      │ memory   │
├────┼────────────────────┼──────────┼──────┼───────────┼──────────┼──────────┤
│ 0  │ test               │ fork     │ 0    │ online    │ 0%       │ 27.5mb   │
└────┴────────────────────┴──────────┴──────┴───────────┴──────────┴──────────┘
[PM2][WARN] Current process list is not synchronized with saved list. App start_bot differs. Type 'pm2 save' to synchronize.
```

Once the program begins, we can view the current status by running *pm2 status:*

```vhdl
$ pm2 status
┌────┬────────────────────┬──────────┬──────┬───────────┬──────────┬──────────┐
│ id │ name               │ mode     │ ↺    │ status    │ cpu      │ memory   │
├────┼────────────────────┼──────────┼──────┼───────────┼──────────┼──────────┤
│ 0  │ test               │ fork     │ 18   │ online    │ 0%       │ 40.8mb   │
└────┴────────────────────┴──────────┴──────┴───────────┴──────────┴──────────┘
[PM2][WARN] Current process list is not synchronized with saved list. App start_bot differs. Type 'pm2 save' to synchronize.
```

While *pm2* was mainly built to run *nodejs* programs, it can handle others, such as python programs:

```bash
$ pm2 start test.py
[PM2] Starting /home/kd/tinkering/test.py in fork_mode (1 instance)
[PM2] Done.
┌────┬────────────────────┬──────────┬──────┬───────────┬──────────┬──────────┐
│ id │ name               │ mode     │ ↺    │ status    │ cpu      │ memory   │
├────┼────────────────────┼──────────┼──────┼───────────┼──────────┼──────────┤
│ 0  │ test               │ fork     │ 37   │ online    │ 100%     │ 37.3mb   │
│ 1  │ test               │ fork     │ 0    │ online    │ 0%       │ 4.0kb    │
└────┴────────────────────┴──────────┴──────┴───────────┴──────────┴──────────┘
[PM2][WARN] Current process list is not synchronized with saved list. App start_bot differs. Type 'pm2 save' to synchronize.
```

We see that *pm2* assigns an ID to every program started. We can use this id to view the output or stop the program:

```bash
$ pm2 logs 0
[TAILING] Tailing last 15 lines for [0] process (change the value with --lines option)
/home/kd/.pm2/logs/test-error.log last 15 lines:
/home/kd/.pm2/logs/test-out.log last 15 lines:
0|test     | hello
0|test     | hello
0|test     | hello
0|test     | hello
0|test     | hello
0|test     | hello
0|test     | hello
0|test     | hello
0|test     | hello
0|test     | hello
0|test     | hello
0|test     | hello
0|test     | hello
0|test     | hello
0|test     | hello
```

```bash
$  pm2 stop 0
[PM2] Applying action stopProcessId on app [0](ids: [ '0' ])
[PM2] [test](0) ✓
┌────┬────────────────────┬──────────┬──────┬───────────┬──────────┬──────────┐
│ id │ name               │ mode     │ ↺    │ status    │ cpu      │ memory   │
├────┼────────────────────┼──────────┼──────┼───────────┼──────────┼──────────┤
│ 0  │ test               │ fork     │ 94   │ stopped   │ 0%       │ 0b       │
│ 1  │ test               │ fork     │ 15   │ errored   │ 0%       │ 0b       │
└────┴────────────────────┴──────────┴──────┴───────────┴──────────┴──────────┘
[PM2][WARN] Current process list is not synchronized with saved list. App start_bot differs. Type 'pm2 save' to synchronize.
```

We wrote both programs to print “hello” and exit, and *pm2* tries to restart them every time they exit. So, we see a stream of lines saying “hello” in the output.

## 9. Conclusion[](https://www.baeldung.com/linux/detach-process-from-terminal#conclusion)

In this tutorial, we looked at several ways to run programs detached from the terminal.

We can **use the *&* operator, and the *nohup*, *disown*, *setsid*, and *screen* commands to start a process detached from the terminal.** However, **to detach a process that has already started, we need to use the *bg* command** after pausing the process using *Ctrl+Z*.

También analizamos el  comando ***pm2* que podemos usar para escenarios más elaborados** , como la ejecución de servidores de aplicaciones. Sin embargo, esto no viene incluido con las distribuciones comunes de Linux de forma predeterminada. Necesitamos instalarlo junto con otras dependencias.

Si tiene algunos años de experiencia en el ecosistema de Linux y está interesado en compartir esa experiencia con la comunidad, consulte nuestras [**Pautas de contribución**](https://www.baeldung.com/linux/contribution-guidelines) .

¡Los comentarios están cerrados en este artículo!