#ifndef LIBLION_API_H
#define LIBLION_API_H

#include <stdlib.h>

// Base URL for the API
extern const char* BASE_URL;

// License structure
typedef struct {
    char* license_key;    // License key string
    char* created_at;      // Creation timestamp
    char* expires_at;      // Expiration timestamp
    int is_active;         // Activation status (1 = active, 0 = inactive)
} License;

// User structure
typedef struct {
    int id;                // User ID
    char* username;        // Username string
    int is_admin;          // Admin status (1 = admin, 0 = regular user)
} User;

/**
 * Creates a new license (Admin only)
 * 
 * @param username Admin username
 * @param password Admin password
 * @param duration_days License duration in days
 * @param user_id Optional user ID to associate (0 for none)
 * @return License object (members will be NULL on failure)
 */
License create_license(const char* username, const char* password, 
                      int duration_days, int user_id);

/**
 * Checks license validity
 * 
 * @param license_key License key to check
 * @return License object (members will be NULL on failure)
 */
License check_license(const char* license_key);

/**
 * Creates a new user (Admin only)
 * 
 * @param admin_user Admin username
 * @param admin_pass Admin password
 * @param username New username
 * @param password New password
 * @param is_admin Admin privilege (1 = admin, 0 = regular)
 * @return 1 on success, 0 on failure
 */
int create_user(const char* admin_user, const char* admin_pass,
               const char* username, const char* password, int is_admin);

/**
 * Frees memory allocated in a License object
 * 
 * @param lic Pointer to License to free
 */
void free_license(License *lic);

#endif /* LIBLION_API_H */
