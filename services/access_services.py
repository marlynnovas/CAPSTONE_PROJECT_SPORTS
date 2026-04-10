#from --- import ---
#from --- import ---

class AccessService:
    @staticmethod
    def validate_access(member_id):
        """
        Valida el acceso de un miembro y registra el intento.
        Versión unificada para la UI de develop y el motor robusto.
        """
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()

            membership = MembershipService.get_active_membership(member_id)

            if not membership:
                result = "denied"
                message = "Sin membresía registrada"
            else:
                status = MembershipService.refresh_membership_status(membership)
                if status == "active":
                    result = "granted"
                    message = "Acceso Permitido"
                else:
                    result = "denied"
                    message = f"Membresía {status}"

            cursor.execute("""
                INSERT INTO access_logs (member_id, granted, message)
                VALUES (?, ?, ?)
            """, (member_id, result == "granted", message))

            conn.commit()
            return {"result": result, "message": message}
        except Exception as e:
            print(f"Error in access validation: {e}")
            return {"result": "denied", "message": "Error de sistema"}
        finally:
            if conn: conn.close()
